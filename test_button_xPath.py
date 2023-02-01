#https://ultimateqa.com/simple-html-elements-for-automation/
#click a button by xPath

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://ultimateqa.com/simple-html-elements-for-automation/')
    page.click('//*[@id="post-909"]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/a')
    print(page.title())
    browser.close  
    