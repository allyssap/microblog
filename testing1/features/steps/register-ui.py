from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

@given(u'the user is on the register page')
def open_browser(context):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)
    context.driver.implicitly_wait(15)
    context.driver.get("http://localhost:8000/auth/register")

@then(u'the page should have a text field to enter the username')
def check_username_textbox(context):
    status = context.driver.find_element(By.NAME, "username").is_displayed()
    assert status is True

@then(u'the page should have a text field to enter the email')
def check_email_textbox(context):
    status = context.driver.find_element(By.NAME, "email").is_displayed()
    assert status is True

@then(u'the page should have a text field to enter the password')
def check_email_textbox(context):
    status = context.driver.find_element(By.NAME, "password").is_displayed()
    assert status is True

@then(u'the page should have a text field to confirm the password')
def check_email_textbox(context):
    status = context.driver.find_element(By.NAME, "password2").is_displayed()
    assert status is True

@then(u'the page should have a button to register')
def check_task_add_button(context):
    status = context.driver.find_element(By.NAME, "submit").is_displayed()
    assert status is True