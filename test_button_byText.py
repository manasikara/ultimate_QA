#https://ultimateqa.com/simple-html-elements-for-automation/
#click a button by text

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://ultimateqa.com/simple-html-elements-for-automation/')
    page.click('text=Click me using this link text!')
    print(page.title())
    browser.close
    