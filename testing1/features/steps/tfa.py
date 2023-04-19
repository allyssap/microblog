from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y%H%M%S")

@given(u'I am a registered user for tfa')
def creating_account(context):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)
    context.driver.implicitly_wait(15)
    context.driver.get("http://localhost:8000/auth/register")
    field = context.driver.find_element(By.NAME, "username")
    field.send_keys(date_time+"tfaT")
    field = context.driver.find_element(By.NAME, "email")
    field.send_keys(date_time+"tfaT@gmail.com")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Testing1!")
    field = context.driver.find_element(By.NAME, "password2")
    field.send_keys("Testing1!")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    context.driver.implicitly_wait(15)
    time.sleep(1)
    context.driver.get("http://localhost:8000/auth/login")



@when(u'I try to login my account')
def step_impl(context):
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"tfaT")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Testing1!")
    context.driver.implicitly_wait(15)

@when(u'I choose the PIN code option to login')
def step_impl(context):
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    context.driver.implicitly_wait(15)

@then(u'my mobile phone will receive a PIN code from Microblog')
def step_impl(context):
    dump_text = context.driver.page_source
    assert ("Check your email for your OTP" in dump_text) is True

@then(u'I enter this PIN code for verification')
def step_impl(context):
    #otp
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"tfaT")
    field = context.driver.find_element(By.NAME, "OTP")
    field.send_keys("1234")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)


@then(u'I login to my account')
def step_impl(context):
    testingURL = context.driver.current_url
    print(str(testingURL))
    assert ("index" in str(testingURL)) is True




@when(u'I choose the verification link option to login')
def step_impl(context):
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    context.driver.implicitly_wait(15)
    time.sleep(1)
    status = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Click to Send!").is_displayed()
    assert status is True
    change_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Click to Send!")
    change_button.click()
    context.driver.implicitly_wait(15)
    time.sleep(1)

@then(u'my email inbox will receive a verification link from Microblog')
def step_impl(context):
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"tfaT")
    status = context.driver.find_element(By.NAME, "submit").is_displayed()
    assert status is True
    change_button = context.driver.find_element(By.NAME, "submit")
    change_button.click()
    context.driver.implicitly_wait(15)
    time.sleep(1)
    dump_text = context.driver.page_source
    assert ("One Time link has been sent" in dump_text) is True

@then(u'click this verification link')
def step_impl(context):
    context.driver.get("http://localhost:8000/auth/verification")
    time.sleep(1)


@then(u'I login to my account by one time link')
def step_impl(context):
    field = context.driver.find_element(By.NAME, "username")
    field.send_keys(date_time+"tfaT")
    field = context.driver.find_element(By.NAME, "email")
    field.send_keys(date_time+"tfaT@gmail.com")
    change_button = context.driver.find_element(By.NAME, "submit")
    change_button.click()
    time.sleep(1)
    testingURL = context.driver.current_url
    assert ("index" in str(testingURL)) is True