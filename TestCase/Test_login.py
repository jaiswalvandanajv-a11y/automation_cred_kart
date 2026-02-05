import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.Cred_Login_Page import LoginPage

def test_login1():
    driver = webdriver.Chrome()
    obj = LoginPage(driver)
    driver.get("https://automation.credence.in/login")
    obj.Enter_email("vandanaj1212@gmail.com")
    obj.Enter_password("vandana121123")
    obj.click_login()
    time.sleep(10)
    print("closing browser")
    driver.close()


