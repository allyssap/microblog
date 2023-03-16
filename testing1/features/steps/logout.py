from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y%H%M%S")

@given(u'I am a registered user')
def creating_account(context):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)
    context.driver.implicitly_wait(15)
    context.driver.get("http://127.0.0.1:5000/auth/register")
    field = context.driver.find_element(By.NAME, "username")
    field.send_keys(date_time+"logoutT")
    field = context.driver.find_element(By.NAME, "email")
    field.send_keys(date_time+"logoutT@gmail.com")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Testing1!")
    field = context.driver.find_element(By.NAME, "password2")
    field.send_keys("Testing1!")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    context.driver.implicitly_wait(15)
    time.sleep(1)



@when(u'I try to logout my account')
def step_impl(context):
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"logoutT")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Testing1!")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    #otp
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"logoutT")
    field = context.driver.find_element(By.NAME, "OTP")
    field.send_keys("1234")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)


@when(u'I click the “Logout” button on the top-right corner')
def step_impl(context):
    status = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").is_displayed()
    assert status is True
    logout_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
    logout_button.click()
    time.sleep(1)
    context.driver.implicitly_wait(15)

@then(u'I get a notification tells me my account successfully logout')
def step_impl(context):
    dump_text = context.driver.page_source
    assert ("Please log in to access this page" in dump_text) is True

@then(u'I stay in the main page of Microblog as I haven’t login status')
def step_impl(context):
    testingURL = context.driver.current_url
    # print(str(testingURL))
    assert ("login" in str(testingURL)) is True