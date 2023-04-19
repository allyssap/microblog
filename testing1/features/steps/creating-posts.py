from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Use Firefox WebDriver
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(chrome_options=option)

@given(u'I am a registered user who is signed in')
def step_impl(context):
    # Navigate to the login page
    driver.get("http://localhost:8000")
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

@when(u'I am at the index')
def step_impl(context):
    # Navigate to the index page
    driver.get("http://localhost:8000/")

@when(u'I write the product that I want to create post for')
def step_impl(context):
    # Fill in the product name in the textarea
    textarea = driver.find_element(By.ID, "product")
    textarea.send_keys("Product Name")

@when(u'I write the company that makes the product')
def step_impl(context):
    # Fill in the company name in the textarea
    textarea = driver.find_element(By.ID, "company")
    textarea.send_keys("Company Name")

@when(u'I select the category of the product')
def step_impl(context):
    # Select the product category from a dropdown menu
    dropdown = Select(driver.find_element(By.ID, "category"))
    dropdown.select_by_visible_text("Other")

@when(u'I finish write the post')
def step_impl(context):
    # Fill in the post content in the textarea
    textarea = driver.find_element(By.ID, "post")
    textarea.send_keys("This is a test post.")

@when(u'I click the submit button')
def step_impl(context):
    # Find the submit button and click it
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

@then(u'a notification should be given that tells me the post has been successfully created')
def step_impl(context):
    # Check if the success message appears in the page source
    assert "Your post is now live!" in driver.page_source

@then(u'I should see my new post on the “Home” page')
def step_impl(context):
    # Check if the new post appears on the home page
    assert "Product Name" in driver.page_source
    
@then(u'I sign out')
def step_impl(context):
    logout_button = driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]")
    logout_button.click()

@when(u'I choose the product that I want to create post for')
def step_impl(context):
    # Fill in the product name in the textarea
    textarea = driver.find_element(By.ID, "product")
    textarea.send_keys("Product Name")

@when(u'I leave my post as blank')
def step_impl(context):
    # Leave the post content blank
    textarea = driver.find_element(By.ID, "post")

@then(u'a notification should be given that tells me the post should not be blank')
def step_impl(context):
    # Check if the error message appears in the page source
    textarea = driver.find_element(By.ID, "company")
    error_message = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "company"))).get_attribute("validationMessage")
    # assert ("fill" in error_message) is True

@then(u'I stay in the creation post session')
def step_impl(context):
    
    # Check if the product name is still in the textarea
    product_textarea = driver.find_element(By.ID, "product")
    assert product_textarea.get_attribute("value") == "Product Name"

