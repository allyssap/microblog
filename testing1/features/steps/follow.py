from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y%H%M%S")

@given(u'the user is viewing another user’s profile')
def view_another(context):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)
    context.driver.implicitly_wait(15)
    context.driver.get("http://127.0.0.1:5000/auth/register")
    #first user create
    field = context.driver.find_element(By.NAME, "username")
    field.send_keys(date_time+"followT1")
    field = context.driver.find_element(By.NAME, "email")
    field.send_keys(date_time+"followT1@gmail.com")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys(date_time)
    field = context.driver.find_element(By.NAME, "password2")
    field.send_keys(date_time)
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    context.driver.implicitly_wait(15)
    time.sleep(1)
    #first user login
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"followT1")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys(date_time)
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    #first user posts
    post_field = context.driver.find_element(By.NAME, "post")
    post_field.send_keys("first post from testing 1")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    post_field = context.driver.find_element(By.NAME, "post")
    post_field.send_keys("second post from testing 1")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    #first user logout
    logout_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
    logout_button.click()
    time.sleep(1)
    #second user create
    logout_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Click to Register!")
    logout_button.click()
    time.sleep(1)
    field = context.driver.find_element(By.NAME, "username")
    field.send_keys(date_time+"followT2")
    field = context.driver.find_element(By.NAME, "email")
    field.send_keys(date_time+"followT2@gmail.com")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys(date_time)
    field = context.driver.find_element(By.NAME, "password2")
    field.send_keys(date_time)
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    context.driver.implicitly_wait(15)
    time.sleep(1)
    #second user login
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"followT2")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys(date_time)
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    #go to explore page
    p_link = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Explore")
    p_link.click()
    time.sleep(1)
    #enter user 1 profile through his posts
    p_link = context.driver.find_element(By.PARTIAL_LINK_TEXT, date_time+"followT1")
    p_link.click()
    time.sleep(1)
    testingURL = context.driver.current_url
    assert ("user/"+date_time+"followT1" in str(testingURL)) is True


@when(u'the user clicks follow user')
def step_impl(context):
    status = context.driver.find_element(By.NAME, "submit").is_displayed()
    assert status is True
    f_button = context.driver.find_element(By.NAME, "submit")
    f_button.click()
    context.driver.implicitly_wait(15)
    time.sleep(1)


@then(u'another user’s followers count should be increased by 1')
def step_impl(context):
    dump_text = context.driver.page_source
    assert ("1 followers" in dump_text) is True

@then(u'current user’s followings count should be increased by 1')
def step_impl(context):
    p_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Profile")
    p_button.click()
    time.sleep(1)
    dump_text = context.driver.page_source
    assert ("1 following" in dump_text) is True







@given(u'the user is following other users')
def step_impl(context):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)
    context.driver.implicitly_wait(15)
    context.driver.get("http://127.0.0.1:5000/")
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"followT2")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys(date_time)
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    home_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Home")
    home_button.click()
    time.sleep(1)
    dump_text = context.driver.page_source
    assert (date_time+"followT1" in dump_text) is True


@when(u'the user is viewing the timeline in Home page')
def step_impl(context):
    testingURL = context.driver.current_url
    assert ("index" in str(testingURL)) is True

@then(u'the list should include posts from followed users')
def step_impl(context):
    dump_text = context.driver.page_source
    assert ("first post from testing 1" in dump_text) is True
    assert ("second post from testing 1" in dump_text) is True

@given(u'the user is viewing another users profile')
def view_another(context):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)
    context.driver.implicitly_wait(15)
    context.driver.get("http://127.0.0.1:5000/")
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"followT2")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys(date_time)
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    time.sleep(1)
    p_link = context.driver.find_element(By.PARTIAL_LINK_TEXT, date_time+"followT1")
    p_link.click()
    time.sleep(1)
    testingURL = context.driver.current_url
    assert ("user/"+date_time+"followT1" in str(testingURL)) is True

@when(u'the user clicks Unfollow user')
def step_impl(context):
    status = context.driver.find_element(By.NAME, "submit").is_displayed()
    assert status is True
    f_button = context.driver.find_element(By.NAME, "submit")
    f_button.click()
    context.driver.implicitly_wait(15)
    time.sleep(1)

@then(u'another user’s followers count should be decreased by 1')
def step_impl(context):
    dump_text = context.driver.page_source
    assert ("0 followers" in dump_text) is True

@then(u'current user’s followings count should be decreased by 1')
def step_impl(context):
    p_button = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Profile")
    p_button.click()
    time.sleep(1)
    dump_text = context.driver.page_source
    assert ("0 following" in dump_text) is True