from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Assuming context.driver is set up elsewhere (e.g., in a before_scenario hook)

@given('I am on the login page')
def step_given_login_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Replace with your login URL


@when('I enter {username} and {password}')
def step_when_enter_credentials(context, username, password):
    username_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'username'))
    )
    username_field.send_keys(username)

    password_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'password'))
    )
    password_field.send_keys(password)


@when('I click the login button')
def step_when_click_login(context):
    login_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'login'))
    )
    login_button.click()


@then('I should see the dashboard')
def step_then_see_dashboard(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/dashboard")  # Adjust the condition to verify the dashboard URL
    )
    assert "Dashboard" in context.driver.title  # Modify as needed to check for dashboard elements


@then('I should see an error message')
def step_then_see_error_message(context):
    error_message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'error'))  # Replace with the actual error class
    )
    assert error_message.is_displayed(), "Error message should be displayed"


@when('I click the "Forgot Password" link')
def step_when_click_forgot_password(context):
    forgot_password_link = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Forgot Password"))
    )
    forgot_password_link.click()


@then('I should be redirected to the password recovery page')
def step_then_redirected_to_recovery_page(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/password-recovery")  # Adjust this URL as needed
    )
    assert "Password Recovery" in context.driver.title  # Modify as needed to check for elements on recovery page
