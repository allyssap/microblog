from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

@given(u'the user is on the register page')
def open_browser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.implicitly_wait(5)
    context.driver.get("http://127.0.0.1:5000/")

@then(u'the page should have a text field to enter the username')
def check_username_textbox(context):
    status = context.driver.find_element(By.NAME, "Username").is_displayed()
    assert status is True

@then(u'the page should have a text field to enter the email')
def check_email_textbox(context):
    status = context.driver.find_element(By.NAME, "Email").is_displayed()
    assert status is True

@then(u'the page should have a text field to enter the password')
def check_email_textbox(context):
    status = context.driver.find_element(By.NAME, "Password").is_displayed()
    assert status is True

@then(u'the page should have a text field to confirm the password')
def check_email_textbox(context):
    status = context.driver.find_element(By.NAME, "Repeat Password").is_displayed()
    assert status is True

@then(u'the page should have a button to register')
def check_task_add_button(context):
    status = context.driver.find_element(By.XPATH, "//button[contains(text(),'Register')]").is_displayed()
    assert status is True