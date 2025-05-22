import asyncio
from pyppeteer import launch

async def connect_siwa_testnet():
    browser = await launch(headless=False)  # Show browser for debugging
    page = await browser.newPage()

    # Navigate to Siwa Testnet URL (replace with actual URL)
    await page.goto('https://siwa-testnet.example.com')

    # Wait for wallet connect button and click it
    await page.waitForSelector('button.connect-wallet')  # Adjust selector
    await page.click('button.connect-wallet')

    # Handle wallet popup or iframe if any (e.g., MetaMask)
    # You may need to switch to popup window or iframe and approve connection

    # Example: wait for connect confirmation element
    await page.waitForSelector('.wallet-connected')  # Adjust selector

    print("Wallet connected to Siwa Testnet!")

    # Add further automation: send tx, check balance, etc.

    await asyncio.sleep(10)  # Keep browser open to observe
    await browser.close()

asyncio.run(connect_siwa_testnet())
