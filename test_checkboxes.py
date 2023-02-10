#https://ultimateqa.com/simple-html-elements-for-automation/
#checkboxes with Neemo https://youtu.be/Cmj6nHhR6BE

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo= 600)
    page = browser.new_page()
    page.goto('https://ultimateqa.com/simple-html-elements-for-automation/')
    page.wait_for_timeout(3000)
    
    #1st
    page.locator('//*[@id="post-909"]/div/div[1]/div/div[3]/div/div[1]/div[8]/div/div/div/form/input[1]').check()
    assert page.locator('//*[@id="post-909"]/div/div[1]/div/div[3]/div/div[1]/div[8]/div/div/div/form/input[1]').is_checked()
    
    #2nd
    page.locator('//*[@id="post-909"]/div/div[1]/div/div[3]/div/div[1]/div[8]/div/div/div/form/input[2]').check()
    assert page.locator('//*[@id="post-909"]/div/div[1]/div/div[3]/div/div[1]/div[8]/div/div/div/form/input[2]').is_checked()
    
    
    browser.close  
    print(page.title())
    print('Done!')              
    