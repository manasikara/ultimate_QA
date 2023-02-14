#https://ultimateqa.com/simple-html-elements-for-automation/
#open toggle to read text

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo= 600)
    page = browser.new_page()
    page.goto('https://ultimateqa.com/simple-html-elements-for-automation/')
    page.click('text=Open toggle to read text')
    time.sleep(3)
    page.click('text=Open toggle to read text')
    time.sleep(3)    
    
    browser.close  
    print(page.title())
    print('Done!')
    