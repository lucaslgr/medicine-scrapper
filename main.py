import asyncio
from pyppeteer import launch


async def main():
    # Launch the browser
    browser = await launch(headless=False)
    page = await browser.newPage()

    # Navigate to the website
    await page.goto("https://www.drogasil.com.br/")

    # Wait for the search input to appear
    await page.waitForSelector("#searchHeader")

    # Input the desired product name
    product_name = "floratil"  # Replace with the desired product name
    await page.type("#searchHeader", product_name)

    # Press Enter to search for the product
    await page.keyboard.press("Enter")

    # Wait for the search results to load
    await page.waitForSelector(".product-item")

    # Get the price of the first product
    price = await page.evaluate(
        """() => {
        const priceElement = document.querySelectorAll(".product-item")[0].querySelector("[data-qa='price_from_item']");
        return priceElement.innerText;
    }"""
    )

    # Print the price
    print("Price:", price)

    # Close the browser
    await browser.close()


# Run the main function
asyncio.get_event_loop().run_until_complete(main())
