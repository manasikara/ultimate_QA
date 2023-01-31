#https://ultimateqa.com/simple-html-elements-for-automation/
#click a button using Name

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://ultimateqa.com/simple-html-elements-for-automation/')
    page.locator("[name=button1]").click
    print(page.title())
    browser.close
    