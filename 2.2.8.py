from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:

    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/file_input.html')

    first_name = browser.find_element(By.XPATH,"/html/body/div/form/div/input[1]")
    first_name.send_keys("Nata")

    last_name = browser.find_element(By.XPATH,"/html/body/div/form/div/input[2]")
    last_name.send_keys("Trifo")

    email = browser.find_element(By.XPATH,"/html/body/div/form/div/input[3]")
    email.send_keys("nata@mail.ru")

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(cur_dir, 'Nata1.txt')
    element = browser.find_element(By.XPATH, "//input[@id='file']")
    element.send_keys(file_path)


    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button.click()

finally:
    time.sleep(7)
    browser.quit()