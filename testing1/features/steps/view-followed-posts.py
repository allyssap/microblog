from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

@given(u'I am a registered user who is logged in')
def step_impl(context):
    driver.get("http://localhost:5000")
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME,"password")
    username_field.send_keys("noah")
    password_field.send_keys("Test1234!")
    sign_in_button = driver.find_element(By.ID, "submit")
    sign_in_button.click()
    username_field = driver.find_element(By.ID, "username")
    opt_field = driver.find_element(By.ID,"OTP")
    username_field.send_keys("noah")
    opt_field.send_keys("1234")
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

@when(u'I navigate to the “Home” tab')
def step_impl(context):
    explore_button = driver.find_element(By.XPATH, "//a[contains(text(),'Explore')]")
    explore_button.click()

@then(u'posts that are posted by the people I follow will be displayed on the Home page')
def step_impl(context):
    posts = driver.find_elements(By.XPATH, "//div[contains(@class,'table')]/table")
    for post in posts:
        post_user = driver.find_element(By.CLASS_NAME, "user_popup")
        post_user_href = post_user.get_attribute("href")
        assert "/user/noah" not in post_user_href
