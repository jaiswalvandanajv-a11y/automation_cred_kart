from selenium import webdriver
from selenium.webdriver.common.by import By


class RegisterPage:

    name_id = (By.ID,"name")
    email_id = (By.ID,"email")
    password_id = (By.ID,"password")
    confirm_id = (By.ID,"password-confirm")
    register_button_xpath = (By.XPATH,"//button[@class='btn btn-primary']")


    def __init__(self,driver):
        self.driver = driver

    def Enter_name(self,name):
        ele_name = self.driver.find_element(*self.name_id).send_keys(name)

    def Enter_email(self,email):
        ele_email = self.driver.find_element(*self.email_id).send_keys(email)

    def Enter_password(self,password):
        ele_password = self.driver.find_element(*self.password_id).send_keys(password)

    def Enter_confirm(self,confirm_pass):
        ele_confirm = self.driver.find_element(*self.confirm_id).send_keys(confirm_pass)

    def Click_regis_button(self):
        click_button = self.driver.find_element(*self.register_button_xpath).click()

