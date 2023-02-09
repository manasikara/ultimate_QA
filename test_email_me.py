#https://ultimateqa.com/simple-html-elements-for-automation/
#fill up the email form

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=900)
    page = browser.new_page()
    page.goto('https://ultimateqa.com/simple-html-elements-for-automation/')
    page.locator('#et_pb_contact_name_0').fill('slawek')
    page.locator('#et_pb_contact_email_0').fill('me@googlemail.com')
    page.locator('.et_pb_contact_submit et_pb_button').click
    
    browser.close
    print('Done')