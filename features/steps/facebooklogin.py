from behave import *
from behave.configuration import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Launch chrome browsers')
def launch_browser(context):
    chrome_opt=Options()
    chrome_opt.add_experimental_option('detach',True)
    context.driver=webdriver.Chrome(options=chrome_opt)

@when('open Fb homepage')
def open_page(context):
    context.driver.get("https://www.facebook.com/")

@then('Enter User name And Password')
def user_pwd(context):
    username_field=WebDriverWait(context.driver,10).until(EC.visibility_of_element_located((By.NAME,'email')))
    username_field.send_keys("9623873895")

    password_field=WebDriverWait(context.driver,10).until(EC.visibility_of_element_located((By.NAME,'pass')))
    password_field.send_keys("Garudzep@10")

    login_btn=context.driver.find_element(By.NAME,'login')
    login_btn.click()

@then('close browsers')
def close_browser(context):
    context.driver.quit()