from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from datetime import datetime


now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y%H%M%S")

@given(u'the user is on the profile page')
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
    field.send_keys(date_time+"pUI")
    field = context.driver.find_element(By.NAME, "email")
    field.send_keys(date_time+"pUI@gmail.com")
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
    name_field.send_keys(date_time+"pUI")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Testing1!")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    #otp
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"pUI")
    field = context.driver.find_element(By.NAME, "OTP")
    field.send_keys("1234")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    #add a post
    post_field = context.driver.find_element(By.NAME, "product")
    post_field.send_keys("test post p1")
    post_field = context.driver.find_element(By.NAME, "company")
    post_field.send_keys("test post c1")
    post_field = context.driver.find_element(By.NAME, "post")
    post_field.send_keys("test post")
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


@then(u'the page should have the text to show the username')
def check_username(context):
    dump_text = context.driver.page_source
    assert ("User: "+date_time+"pUI" in dump_text) is True

@then(u'the page should have a text to show the last login information')
def check_login_info(context):
    dump_text = context.driver.page_source
    assert ("Last seen on" in dump_text) is True


@then(u'the page should have a text to show the followers number')
def check_followers(context):
    dump_text = context.driver.page_source
    assert ("followers" in dump_text) is True

@then(u'the page should have a text to show the followings number')
def check_followings(context):
    dump_text = context.driver.page_source
    assert ("following" in dump_text) is True

@then(u'the page should have a button to modify the profile')
def check_modify_button(context):
    dump_text = context.driver.page_source
    assert ("Edit your profile" in dump_text) is True

@then(u'the page should have a place to show the history posts')
def check_historys(context):
    dump_text = context.driver.page_source
    assert ("test post" in dump_text) is True