#https://ultimateqa.com/simple-html-elements-for-automation/
#xpath button 1

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo= 600)
    page = browser.new_page()
    page.goto('https://ultimateqa.com/simple-html-elements-for-automation/')
    
    time.sleep(10)
    
    #close the pop-up window
    page.get_by_role("button", name="Close").click()
    
    #click the "XPath tutorial for automation testers"
    page.get_by_role("button", name="Xpath Button 1").first.click()
    
    page.goto("https://ultimateqa.com/simple-html-elements-for-automation/")
    
    #click the "2. Button 2 - same exact button, different place in the HTML"
    page.get_by_role("button", name="Xpath Button 1").nth(1).click()
    
    page.goto("https://ultimateqa.com/simple-html-elements-for-automation/")
    
    #click the "Xpath with different button text"
    page.get_by_role("button", name="Xpath Button 1").nth(2).click()
    
    page.goto("https://ultimateqa.com/simple-html-elements-for-automation/")
    
    #click the "2. Button 2 - same exact button, different place in the HTML"
    page.get_by_role("button", name="Xpath Button 2").click()
    
    
    
    print(page.title())
    browser.close  
    print('Done!')
   