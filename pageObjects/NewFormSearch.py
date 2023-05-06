import time
from selenium.webdriver.support.ui import Select
# from selenium import webdriver
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# from selenium.webdriver import Keys
# from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys


class NewFormSearch:
    textbox_FormName_css_selector = "input#Searchforms.inpSearch"

    def __init__(self,driver):
        # self.listitem = None
        self.driver = driver

    def editNewFormSearch(self):
        self.driver.find_element(By.CSS_SELECTOR,self.textbox_FormName_css_selector).clear()
        self.driver.find_element(By.CSS_SELECTOR,self.textbox_FormName_css_selector).click()

    def addNewFormSearch(self,formname):
        self.driver.find_element(By.CSS_SELECTOR,self.textbox_FormName_css_selector).send_keys(formname)

    def downNewFormSearch(self):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_FormName_css_selector).send_keys(Keys.DOWN)

    def enterNewFormSearch(self):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_FormName_css_selector).send_keys(Keys.ENTER)


