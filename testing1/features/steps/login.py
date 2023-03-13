from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y%H%M%S")

@given(u'I have registered an account')
def creating_account(context):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)
    context.driver.implicitly_wait(15)
    context.driver.get("http://127.0.0.1:5000/auth/register")
    field = context.driver.find_element(By.NAME, "username")
    field.send_keys(date_time+"loginT")
    field = context.driver.find_element(By.NAME, "email")
    field.send_keys(date_time+"loginT@gmail.com")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Testing1!")
    field = context.driver.find_element(By.NAME, "password2")
    field.send_keys("Testing1!")
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    context.driver.implicitly_wait(15)
    time.sleep(1)
    context.driver.get("http://127.0.0.1:5000/auth/login")



@when(u'I attempt to fill in the login info')
def step_impl(context):
    name_field = context.driver.find_element(By.NAME, "username")
    name_field.send_keys(date_time+"loginT")
    field = context.driver.find_element(By.NAME, "password")
    field.send_keys("Testing1!")

@when(u'click the login button')
def step_impl(context):
    add_button = context.driver.find_element(By.NAME, "submit")
    add_button.click()
    context.driver.implicitly_wait(15)

@then(u'I will log in to my account')
def step_impl(context):
    time.sleep(1)
    dump_text = context.driver.page_source
    assert ("Hi, "+date_time+"loginT!" in dump_text) is True

@then(u'I will view my home page')
def step_impl(context):
    testingURL = context.driver.current_url
    print(str(testingURL))
    assert ("index" in str(testingURL)) is True