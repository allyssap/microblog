from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

@given(u'I am a user who is signed in')
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

@when(u'I go to the profile page')
def step_impl(context):
    # Navigate to the home page
    profile_button = driver.find_element(By.XPATH, "//a[contains(text(),'Profile')]")
    profile_button.click()

@then(u'all my existing posts should be displayed in the page')
def step_impl(context):
    posts = driver.find_elements(By.XPATH, "//div[contains(@class,'table')]/table")
    for post in posts:
        driver.find_element(By.ID, post).click()
        post_content = driver.find_element(By.XPATH, "//*[@id='post']")
        assert len(post_content.text.strip()) > 0
        driver.back()

@then(u'they are displayed as newest at the top')
def step_impl(context):
    # Verify that existing posts are displayed in the correct order
    posts = driver.find_elements(By.XPATH, "//div[contains(@class,'table')]/table")
    dates = [post.find_element(By.XPATH, ".//span[contains(@class,'flask-moment')]") for post in posts]
    dates_text = [date.get_attribute("data-timestamp") for date in dates]
    assert dates_text == sorted(dates_text, reverse=True)
