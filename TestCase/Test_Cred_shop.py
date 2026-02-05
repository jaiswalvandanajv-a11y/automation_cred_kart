from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from PageObject.Cred_Shoping_Page import Shopping

def test_shopping():

    driver = webdriver.Chrome()
    obj = Shopping(driver)
    driver.get("https://automation.credence.in/shop")
    obj.click_play()
    obj.add_to_cart_play()
    obj.click_continue()
    time.sleep(3)
    obj.click_xbos()
    obj.add_to_cart_xbos()
    time.sleep(10)
    driver.execute_script("window.scrollBy(0, 500);")
    ele_d = obj.quantity_xbos(index=1)
    drop_down = Select(ele_d)
    drop_down.select_by_index(1)
    # drop_down.select_by_index(1)
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, 500);")
    total = obj.validate_total()
    if total== "$1,468.97":
        print("order total is correct")
    else:
        print("order total is incorrect")







    #
    # driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div").click()
    # driver.find_element(By.XPATH,"//input[@class='btn btn-success btn-lg']").click()
    # time.sleep(4)
    # driver.find_element(By.XPATH,"//a[@class='btn btn-primary btn-lg']").click()
    # driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div/div/a[1]/img").click()
    # driver.find_element(By.XPATH,"//input[@class='btn btn-success btn-lg']").click()
    # driver.execute_script("window.scrollBy(0, 500);")
    # drop_ele = driver.find_element(By.XPATH,"/html/body/div/table/tbody/tr[2]/td[3]/select")
    # drop_down = Select(drop_ele)
    # drop_down.select_by_index(1)
    # time.sleep(5)
    # driver.execute_script("window.scrollBy(0, 500);")
    # time.sleep(5)
    # total_ele = driver.find_element(By.XPATH,"//td[@class='table-bg']").text
    # if total_ele == "$1,468.97":
    #     print("order total is correct")
    # else:
    #     print("order total is incorrect")
    #
