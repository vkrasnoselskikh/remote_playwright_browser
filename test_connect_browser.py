import pytest
from playwright.async_api import async_playwright


@pytest.mark.parametrize("anyio_backend", ["asyncio"])
async def test_connect_browser(anyio_backend):
    async with async_playwright() as p:
        browser = await p.chromium.connect("ws://localhost:9002/playwright")
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("http://playwright.dev")
        assert "Playwright" in await page.title()
        print(await page.content())
        await browser.close()
