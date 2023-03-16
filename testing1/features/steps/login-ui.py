from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

@given(u'the user is on the login page')
def open_browser(context):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)
    context.driver.implicitly_wait(15)
    context.driver.get("http://127.0.0.1:5000/auth/login")

@then(u'the page should have a text field to enter the existing username')
def check_username_textbox(context):
    status = context.driver.find_element(By.NAME, "username").is_displayed()
    assert status is True

@then(u'the page should have a text field to enter the existing password')
def check_email_textbox(context):
    status = context.driver.find_element(By.NAME, "password").is_displayed()
    assert status is True


@then(u'the page should have a button to signin')
def check_login_button(context):
    status = context.driver.find_element(By.NAME, "submit").is_displayed()
    assert status is True

@then(u'the page should have an option allows user to register')
def check_resigster_button(context):
    dump_text = context.driver.page_source
    assert ("auth/register" in dump_text) is True

@then(u'the page should have an option allows user to reset password')
def check_resigster_button(context):
    dump_text = context.driver.page_source
    assert ("auth/reset_password_request" in dump_text) is True
