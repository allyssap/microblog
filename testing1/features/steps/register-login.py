from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y%H%M%S")

@given(u'I am a new user')
def open_browser(context):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)
    context.driver.implicitly_wait(15)
    context.driver.get("http://localhost:8000/auth/register")


@when(u'I fill in a unique {username} in the username field')
def step_impl(context,username):
    field = context.driver.find_element(By.NAME, "username")
    field.send_keys("noah")


@when(u'do the same for the {email} field')
def step_impl(context,email):
    field = context.driver.find_element(By.NAME, "email")
    field.send_keys(date_time+"regisT@gmail.com")

@when(u'the {password} field')
def step_impl(context,password):
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Test1234!")


@when(u'confirm the {password}')
def step_impl(context,password):
    field = context.driver.find_element(By.NAME, "password2")
    field.send_keys("Test1234!")


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


