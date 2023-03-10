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
    title_field = context.driver.find_element(By.NAME, "username")
    title_field.send_keys(date_time)


@when(u'do the same for the {email} field')
def step_impl(context,email):
    title_field = context.driver.find_element(By.NAME, "email")
    title_field.send_keys(date_time+"testing@gmail.com")

@when(u'the {password} field')
def step_impl(context,password):
    title_field = context.driver.find_element(By.NAME, "password")
    title_field.send_keys(password)


@when(u'confirm the {password}')
def step_impl(context,password):
    title_field = context.driver.find_element(By.NAME, "password2")
    title_field.send_keys(password)


@when(u'click the register button')
def step_impl(context):
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    context.driver.implicitly_wait(15)


@then(u'the account will be registered')
def step_impl(context):
    context.driver.implicitly_wait(45)
    time.sleep(1)
    # context.driver.get("http://127.0.0.1:5000/auth/login")
    dump_text = context.driver.page_source
    # print(dump_text)
    assert ("Congratulations, you are now a registered user!" in dump_text) is True