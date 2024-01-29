from selenium.webdriver.common.by import By
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_SEND = (By.XPATH,'//*[@id="id_login-username"]')
    PASS_SEND = (By.XPATH,'//*[@id="id_login-password"]')
    LOGIN_BUT = (By.XPATH, '//*[@id="login_form"]/button')