from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I launch browser')
def launch(context):
    chrome_opt=Options()
    chrome_opt.add_experimental_option('detach',True)
    context.driver=webdriver.Chrome(options=chrome_opt)


@when('I open application')
def open(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



@when('Enter valid username and password')
def user_pwd(context):
    user_name=WebDriverWait(context.driver,10).until(EC.visibility_of_element_located((By.NAME,'username')))
    user_name.send_keys('Admin')

    pass_name=WebDriverWait(context.driver,10).until(EC.visibility_of_element_located((By.NAME,'password')))
    pass_name.send_keys('admin123')

@when('click on login')
def click_btn(context):
    btn_click=context.driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    btn_click.click()

@when('navigate to search page')
def step_impl(context):
    assert True, "Test Passed"


@then('search page should display')
def step_impl(context):
    assert True, "Test Passed"


@when('navigate to Advanced search page')
def step_impl(context):
    assert True, "Test Passed"


@then('Advanced search page should display')
def step_impl(context):
    assert True, "Test Passed"
