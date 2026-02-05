from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.Cred_Register_Page import RegisterPage

def test_Registration():
    driver=webdriver.Chrome()
    objc = RegisterPage(driver)
    driver.get("https://automation.credence.in/register")
    objc.Enter_name("vandanajaiswal")
    objc.Enter_email("vandanaj1212@gmail.com")
    objc.Enter_password("vandana121123")
    objc.Enter_confirm("vandana1123")
    objc.Click_regis_button()
    driver.implicitly_wait(20)
    driver.close()









