from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Shopping():

    playstation_xpath = (By.XPATH,"/html/body/div/div[2]/div[1]/div/div")
    play_addtocart_xpath = (By.XPATH,"//input[@class='btn btn-success btn-lg']")
    continue_xpath1 = (By.XPATH,"//a[@class='btn btn-primary btn-lg']")
    xbos_xpath = (By.XPATH,"/html/body/div/div[2]/div[2]/div/div/a[1]/img")
    xbos_addtocart_xpath = (By.XPATH,"//input[@class='btn btn-success btn-lg']")
    xbos_quan_xpath=(By.XPATH,"/html/body/div/table/tbody/tr[2]/td[3]/select")
    total_xpath = (By.XPATH,"//td[@class='table-bg']")

    def __init__(self,driver):
        self.driver = driver

    def click_play(self):
        ele_play = self.driver.find_element(*self.playstation_xpath).click()

    def add_to_cart_play(self):
        ele_add_play = self.driver.find_element(*self.play_addtocart_xpath).click()

    def click_continue(self):
        ele_continue = self.driver.find_element(*self.continue_xpath1).click()

    def click_xbos(self):
        ele_xbos = self.driver.find_element(*self.xbos_xpath).click()

    def add_to_cart_xbos(self):
        ele_add_xbos = self.driver.find_element(*self.xbos_addtocart_xpath).click()

    def quantity_xbos(self,index):
        ele_quan_xbos = self.driver.find_element(*self.xbos_quan_xpath).click()

    def validate_total(self):
        ele_total = self.driver.find_element(*self.total_xpath).text
