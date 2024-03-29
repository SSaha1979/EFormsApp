
# from selenium import webdriver
# driver = webdriver.Chrome()
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id="email"
    textbox_password_id="password"
    button_login_id="btnLogin"
    span_logout_xpath='/html/body/div[2]/div[1]/div/div[2]/div[1]/nav/ul/li/a/span[2]'
    href_logout_xpath='/html/body/div[2]/div[1]/div/div[2]/div[1]/nav/ul/li/ul/li[3]/a'

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID,self.button_login_id).click()

    def spanLogout(self):
        self.driver.find_element(By.XPATH,self.span_logout_xpath).click()

    def hrefLogout(self):
        self.driver.find_element(By.XPATH,self.href_logout_xpath).click()
