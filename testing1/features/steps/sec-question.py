from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y%H%M%S")

@given(u'I am signed in and at my profile page')
def initialize(context):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)
    context.driver.implicitly_wait(15)
    context.driver.get("http://localhost:8000/auth/login")
    #register
    logout_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Click to Register!")
    logout_button.click()
    field = context.driver.find_element(By.NAME, "username")
    field.send_keys(date_time+"secQ")
    field = context.driver.find_element(By.NAME, "email")
    field.send_keys(date_time+"secQ@gmail.com")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Testing1!")
    field = context.driver.find_element(By.NAME, "password2")
    field.send_keys("Testing1!")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    # context.driver.implicitly_wait(15)
    time.sleep(1)
    #login
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"secQ")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Testing1!")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    #otp
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"secQ")
    field = context.driver.find_element(By.NAME, "OTP")
    field.send_keys("1234")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    status = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").is_displayed()
    assert status is True
    logout_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Profile")
    logout_button.click()
    time.sleep(1)
    
    # context.driver.implicitly_wait(15)


@when(u'I clicking ‘edit my profile’')
def step_impl(context):
    status = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Edit your profile").is_displayed()
    assert status is True
    change_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Edit your profile")
    change_button.click()
    time.sleep(1)


@then(u'click ‘set security question’')
def step_impl(context):
    status = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Set Security Question").is_displayed()
    assert status is True
    change_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Set Security Question")
    change_button.click()
    time.sleep(1)

@then(u'enter my question into a text box')
def step_impl(context):
    dump_text = context.driver.page_source
    assert ("What is your mother's maiden name?" in dump_text) is True

@then(u'enter my answer into another text box')
def step_impl(context):
    field = context.driver.find_element(By.NAME, "answer")
    field.send_keys("answer")
    time.sleep(1)


@then(u'click ‘save security question’')
def step_impl(context):
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    context.driver.implicitly_wait(15)

@then(u'my security question will be saved')
def step_impl(context):
    dump_text = context.driver.page_source
    assert ("Your security question has been set" in dump_text) is True
    status = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").is_displayed()
    assert status is True
    logout_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
    logout_button.click()
    time.sleep(1)
    change_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Or Answer Your Security Question")
    change_button.click()
    field = context.driver.find_element(By.NAME, "username")
    field.send_keys(date_time+"secQ")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    field = context.driver.find_element(By.NAME, "answer")
    field.send_keys("answer")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    dump_text = context.driver.page_source
    assert ("Hi" in dump_text) is True
