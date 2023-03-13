from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from datetime import datetime


now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y%H%M%S")

@given(u'I am on profile page')
def initialize(context):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)
    context.driver.implicitly_wait(15)
    context.driver.get("http://127.0.0.1:5000/auth/login")
    #register
    logout_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Click to Register!")
    logout_button.click()
    field = context.driver.find_element(By.NAME, "username")
    field.send_keys(date_time+"changeAm")
    field = context.driver.find_element(By.NAME, "email")
    field.send_keys(date_time+"changeAm@gmail.com")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Tesing1!")
    field = context.driver.find_element(By.NAME, "password2")
    field.send_keys("Tesing1!")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    # context.driver.implicitly_wait(15)
    time.sleep(1)
    #login
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"changeAm")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Tesing1!")
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


@when(u'I click ‘edit profile’')
def check_username(context):
    status = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Edit your profile").is_displayed()
    assert status is True
    change_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Edit your profile")
    change_button.click()
    time.sleep(1)

@then(u'change the text in the about me text box')
def check_login_info(context):
    status = context.driver.find_element(By.NAME, "about_me").is_displayed()
    assert status is True
    field = context.driver.find_element(By.NAME, "about_me")
    field.send_keys("test about me")


@then(u'click submit')
def check_followers(context):
    status = context.driver.find_element(By.NAME, "submit").is_displayed()
    assert status is True
    confirm_button = context.driver.find_element(By.NAME, "submit")
    confirm_button.click()
    time.sleep(1)

@then(u'my about me will be edited')
def check_followings(context):
    dump_text = context.driver.page_source
    assert ("Your changes have been saved." in dump_text) is True
    p_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Profile")
    p_button.click()
    time.sleep(1)
    dump_text = context.driver.page_source
    assert ("test about me" in dump_text) is True