from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y%H%M%S")

@given(u'I am a new user')
def open_browser(context):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)
    context.driver.implicitly_wait(15)
    context.driver.get("http://127.0.0.1:5000/auth/register")


@when(u'I fill in a unique {username} in the username field')
def step_impl(context,username):
    field = context.driver.find_element(By.NAME, "username")
    field.send_keys(date_time)


@when(u'do the same for the {email} field')
def step_impl(context,email):
    field = context.driver.find_element(By.NAME, "email")
    field.send_keys(date_time+"testing@gmail.com")

@when(u'the {password} field')
def step_impl(context,password):
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys(date_time)


@when(u'confirm the {password}')
def step_impl(context,password):
    field = context.driver.find_element(By.NAME, "password2")
    field.send_keys(date_time)


@when(u'click the register button')
def step_impl(context):
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    context.driver.implicitly_wait(15)


@then(u'the account will be registered')
def step_impl(context):
    time.sleep(1)
    dump_text = context.driver.page_source
    assert ("Congratulations, you are now a registered user!" in dump_text) is True




@given(u'I have registered an account')
def step_impl(context):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)
    context.driver.implicitly_wait(5)
    context.driver.get("http://127.0.0.1:5000/auth/login")

@when(u'I attempt to fill in the login info')
def step_impl(context):
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time)
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys(date_time)

@when(u'click the login button')
def step_impl(context):
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    context.driver.implicitly_wait(15)

@then(u'I will log in to my account')
def step_impl(context):
    time.sleep(1)
    dump_text = context.driver.page_source
    assert ("Hi, "+date_time+"!" in dump_text) is True

@then(u'I will view my home page')
def step_impl(context):
    testingURL = context.driver.current_url
    print(str(testingURL))
    assert ("index" in str(testingURL)) is True