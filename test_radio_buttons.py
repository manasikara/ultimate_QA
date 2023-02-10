#https://ultimateqa.com/simple-html-elements-for-automation/
#radio buttons

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo= 600)
    page = browser.new_page()
    page.goto('https://ultimateqa.com/simple-html-elements-for-automation/')
    
    time.sleep(1)
     # ? ? page.get_by_label('').check - does't work for some reason
    page.click('//*[@id="post-909"]/div/div[1]/div/div[3]/div/div[1]/div[7]/div/div/div/form/input[1]')
    page.click('//*[@id="post-909"]/div/div[1]/div/div[3]/div/div[1]/div[7]/div/div/div/form/input[2]')
    page.click('//*[@id="post-909"]/div/div[1]/div/div[3]/div/div[1]/div[7]/div/div/div/form/input[3]')
    
    browser.close  
    print(page.title())
    print('Done!')
    