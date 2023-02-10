#https://ultimateqa.com/simple-html-elements-for-automation/
#dropdown list with Neemo --> https://youtu.be/7rlXvK5cG4w

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=900)
    page = browser.new_page()
    page.goto('https://ultimateqa.com/simple-html-elements-for-automation/')
    page.mouse.wheel(0, 1100)
    page.locator('//*[@id="post-909"]/div/div[1]/div/div[3]/div/div[1]/div[9]/div/div/div/select').select_option(index=3)
    page.wait_for_timeout(3000)
    
    browser.close  
    print(page.title())
    print('Done!')
    