import sys,asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page(viewport={'width':2560,'height':1440})
        for ani in ['perro','gato']:
            for modo in ['banner','perfil']:
                await pg.goto(f'file:///home/claude/marca/marca.html?modo={modo}&ani={ani}')
                await pg.wait_for_function("document.title==='LISTO'")
                el=await pg.query_selector('canvas');await el.screenshot(path=f'/home/claude/marca/{ani}_{modo}.png',omit_background=True)
        await b.close()
asyncio.run(main())
