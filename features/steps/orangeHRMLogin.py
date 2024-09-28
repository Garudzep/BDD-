from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Launch chrome browser')
def launch_browser(context):
    chrome_opt = Options()
    chrome_opt.add_experimental_option('detach', True)
    context.driver = webdriver.Chrome(options=chrome_opt)


@when('open orange hrm homepage')
def open_home_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then('Login Page')
def login_page(context):

    #username_filed=context.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
    #username_filed.send_keys("Admin")
    username_field = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.NAME, 'username')))
    username_field.send_keys("Admin")


    #password_fiels=context.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
    #password_fiels.send_kyes("admin123")
    password_field = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.NAME, 'password')) )
    password_field.send_keys("admin123")


    login_button = context.driver.find_element(By.XPATH, '//*[@type="submit"]')
    login_button.click()


@then('close browser')
def close_browser(context):
    context.driver.quit()

