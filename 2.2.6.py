from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/execute_script.html')
    browser.maximize_window()

    x = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x.text
    y = calc(x)

    answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
    answer.send_keys(y)

    browser.execute_script("window.scrollBy(0, 100);")

    check = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    check.click()

    radio = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    radio.click()

    button = browser.find_element(By.XPATH,"/html/body/div/form/button")
    button.click()
finally:
    time.sleep(5)
    browser.quit()