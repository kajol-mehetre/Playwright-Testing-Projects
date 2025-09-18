from playwright.sync_api import sync_playwright

keyword = "Library"

with sync_playwright() as p:
   browser = p.chromium.launch(headless=False)
   page = browser.new_page()
   page.goto('https://playwright.dev')

    # Open the search bar
   page.click("text = API")

   #wait for results to load
   page.wait_for_selector("h3")

   title = page.title()
   assert keyword in title, f"Keyword '{keyword}' not found in page title"

   print(title)
   browser.close()
