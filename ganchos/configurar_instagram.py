"""Configura el acceso OFICIAL a Instagram (API de Meta) sin que el token pase por el chat.

Pide (con entrada OCULTA, no se ve al escribir): el App ID, el App Secret y el token corto del Graph API Explorer.
Lo cambia por un token largo (~60 dias), busca tu cuenta de Instagram Business conectada a la pagina de Facebook
y guarda todo en secretos/instagram.json. Solo imprime el nombre de la cuenta encontrada.

Uso:  python configurar_instagram.py           (primera vez / renovar el token cada ~60 dias)
      python configurar_instagram.py --todas   (agrega todas las cuentas conectadas usando el token ya guardado)
"""
import json
from getpass import getpass
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlencode

V = "https://graph.facebook.com/v21.0/"


def g(ruta, **p):
    return json.loads(urlopen(V + ruta + "?" + urlencode(p), timeout=40).read())


def guardar(largo, app_id, cuentas):
    Path("secretos").mkdir(exist_ok=True)
    f = Path("secretos/instagram.json")
    datos = {"token": largo, "app_id": app_id, "ig_user_id": cuentas[0]["ig_user_id"], "usuario": cuentas[0]["usuario"],
             "cuentas": cuentas}
    f.write_text(json.dumps(datos, indent=1))
    f.chmod(0o600)
    print("✅ Listo: " + ", ".join("@" + x["usuario"] for x in cuentas) + " guardadas en secretos/instagram.json (el token dura ~60 días).")
    print("   Prueba:  python plataformas.py instagram --tema cafe")


def todas():
    """Reusa el token largo ya guardado y agrega TODAS las cuentas de Instagram conectadas (sin pegar nada)."""
    f = Path("secretos/instagram.json")
    if not f.exists():
        raise SystemExit("⛔ Primero corre:  python configurar_instagram.py")
    d = json.loads(f.read_text())
    paginas = g("me/accounts", fields="name,instagram_business_account{id,username}", access_token=d["token"]).get("data", [])
    cuentas = [{"ig_user_id": p["instagram_business_account"]["id"], "usuario": p["instagram_business_account"].get("username"),
                "pagina": p["name"]} for p in paginas if p.get("instagram_business_account")]
    if not cuentas:
        raise SystemExit("⛔ No encontré cuentas de Instagram conectadas a tus páginas.")
    guardar(d["token"], d.get("app_id"), cuentas)


def main():
    import sys
    if "--todas" in sys.argv:
        return todas()
    print("🔐 Pega cada dato y presiona Enter (no se verá lo que escribes).")
    app_id = getpass("App ID: ").strip()
    secret = getpass("App Secret: ").strip()
    corto = getpass("Token del Graph API Explorer: ").strip()
    try:
        largo = g("oauth/access_token", grant_type="fb_exchange_token", client_id=app_id, client_secret=secret,
                  fb_exchange_token=corto)["access_token"]
    except Exception as e:
        raise SystemExit(f"⛔ No se pudo canjear el token: {str(e)[:120]}. Revisa App ID / Secret y que el token sea reciente.")
    paginas = g("me/accounts", fields="name,instagram_business_account{id,username}", access_token=largo).get("data", [])
    cuentas = [(p["name"], p["instagram_business_account"]) for p in paginas if p.get("instagram_business_account")]
    if not cuentas:
        raise SystemExit("⛔ Ninguna página tiene una cuenta de Instagram Business/Creator conectada. Conéctala en la configuración de la página.")
    for k, (pag, ig) in enumerate(cuentas, 1):
        print(f"  {k}. @{ig.get('username')} (página {pag})")
    r = input("¿Cuáles uso? (Enter = todas · o números separados por coma, ej: 1,2): ").strip() if len(cuentas) > 1 else ""
    elegidas = [cuentas[int(x) - 1] for x in r.replace(" ", "").split(",") if x.isdigit() and 0 < int(x) <= len(cuentas)] if r else cuentas
    guardar(largo, app_id, [{"ig_user_id": ig["id"], "usuario": ig.get("username"), "pagina": pag} for pag, ig in elegidas])


if __name__ == "__main__":
    main()
