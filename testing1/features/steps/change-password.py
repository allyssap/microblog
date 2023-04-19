from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from datetime import datetime


now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y%H%M%S")

@given(u'I am signed in and on my profile page')
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
    field.send_keys(date_time+"changePw")
    field = context.driver.find_element(By.NAME, "email")
    field.send_keys(date_time+"changePw@gmail.com")
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
    name_field.send_keys(date_time+"changePw")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Testing1!")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    #otp
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"changePw")
    field = context.driver.find_element(By.NAME, "OTP")
    field.send_keys("1234")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    #profile
    status = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Profile").is_displayed()
    assert status is True
    logout_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Profile")
    logout_button.click()
    time.sleep(1)
    # context.driver.implicitly_wait(15)


@when(u'I click ‘edit my profile’')
def check_username(context):
    status = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Edit your profile").is_displayed()
    assert status is True
    change_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Edit your profile")
    change_button.click()
    time.sleep(1)

@then(u'click ‘change password’')
def check_login_info(context):
    status = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Change Password").is_displayed()
    assert status is True
    change_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Change Password")
    change_button.click()
    time.sleep(1)


@then(u'enter my current password')
def check_followers(context):
    status = context.driver.find_element(By.NAME, "current_password").is_displayed()
    assert status is True
    pwd = context.driver.find_element(By.NAME, "current_password")
    pwd.send_keys("Testing1!")
    status = context.driver.find_element(By.NAME, "new_password").is_displayed()
    assert status is True
    pwd = context.driver.find_element(By.NAME, "new_password")
    pwd.send_keys("Testing2!")
    status = context.driver.find_element(By.NAME, "confirm_password").is_displayed()
    assert status is True
    pwd = context.driver.find_element(By.NAME, "confirm_password")
    pwd.send_keys("Testing2!")
    submit_button = context.driver.find_element(By.NAME, "submit")
    submit_button.click()
    time.sleep(1)
   

@then(u'I will be prompted to set my new password')
def check_followings(context):
    dump_text = context.driver.page_source
    assert ("Your changes have been saved." in dump_text) is True
    logout_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
    logout_button.click()
    time.sleep(1)
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"changePw")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Testing2!")
    submit_button = context.driver.find_element(By.NAME, "submit")
    submit_button.click()
    time.sleep(1)
    #otp
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"changePw")
    field = context.driver.find_element(By.NAME, "OTP")
    field.send_keys("1234")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    testingURL = context.driver.current_url
    assert ("index" in str(testingURL)) is True