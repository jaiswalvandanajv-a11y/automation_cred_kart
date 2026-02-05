from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    email_id = (By.ID,"email")
    password_id = (By.ID,"password")
    login_button_xpath = (By.XPATH,"//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def Enter_email(self,email):
        ele_email = self.driver.find_element(*self.email_id).send_keys(email)

    def Enter_password(self,password):
        ele_pass = self.driver.find_element(*self.password_id).send_keys(password)

    def click_login(self):
        login_click = self.driver.find_element(*self.login_button_xpath).click()


