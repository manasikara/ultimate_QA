#https://ultimateqa.com/simple-html-elements-for-automation/
#radio buttons

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo= 800)
    page = browser.new_page()
    page.goto('https://ultimateqa.com/simple-html-elements-for-automation/')
    
    # ? ? page.get_by_label('').check
    
    # ? ? page.get_by_label('').check
    
    # ? ? page.get_by_label('').check
    
    browser.close  
    print(page.title())
    print('Done!')
    