import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.keys



class NewFormSubmit:
    drp_Design_css_selector = "select#ddEmpDesignation"
    drp_Location_css_selector = "select#ddEmpLocation"
    drp_Submission_css_selector = "select#drpRequestSubmissionFor"
    chk_Request_xpath = '//*[@id="collapseFour"]/div/div/div[2]/label/span'
    textbox_EmpName_css_selector = "input#txtEmpName_1"
    textbox_EmpID_css_selector = "input#txtEmpID_1"
    textbox_LogicCard_css_selector = "input#txtLogicCardID_1"
    drp_StnName_css_selector = "select#ddlStationName_1"
    drp_Shop_css_selector = "select#ddlShop_1"
    drp_Access_css_selector = "select#ddlAccessGroup_1"
    btn_Add_css_selector = "button.btn.btn-sm.submit-btn"
    btn_Remove_css_selector = "input#remove_2.remove-btn"
    textbox_Business_css_selector = "textarea#txtBusinessJustification.form-control"
    btn_Submit_css_selector = "button#btnSubmit.btn.btn-primary"
    btn_ok_xpath = '//*[@id="modalOkButton"]'


    def __init__(self, driver):
        # self.listitem = None
        self.driver = driver

    def editEmpDesign(self):
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Design_css_selector).click()
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Design_css_selector).send_keys(Keys.DOWN)

    def addEmpDesign(self):
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Design_css_selector).send_keys(Keys.ENTER)

    def editEmpLocation(self):
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Location_css_selector).click()
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Location_css_selector).send_keys(Keys.DOWN)

    def addEmpLocation(self):
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Location_css_selector).send_keys(Keys.ENTER)

    def editEmpSubmission(self):
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Submission_css_selector).click()
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Submission_css_selector).send_keys(Keys.DOWN)

    def addEmpSubmission(self):
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Submission_css_selector).send_keys(Keys.ENTER)

    def clickRequest(self):
        self.driver.find_element(By.XPATH, self.chk_Request_xpath).click()

    def addEmpName(self,empname):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_EmpName_css_selector).click()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_EmpName_css_selector).send_keys(empname)

    def addEmpID(self,empid):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_EmpID_css_selector).click()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_EmpID_css_selector).send_keys(empid)

    def addLogicCard(self,logiccard):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_LogicCard_css_selector).click()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_LogicCard_css_selector).send_keys(logiccard)

    def editStnName(self):
        self.driver.find_element(By.CSS_SELECTOR, self.drp_StnName_css_selector).click()
        self.driver.find_element(By.CSS_SELECTOR, self.drp_StnName_css_selector).send_keys(Keys.DOWN)

    def addStnName(self):
        self.driver.find_element(By.CSS_SELECTOR, self.drp_StnName_css_selector).send_keys(Keys.ENTER)

    def editShop(self):
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Shop_css_selector).click()
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Shop_css_selector).send_keys(Keys.DOWN)

    def addShop(self):
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Shop_css_selector).send_keys(Keys.ENTER)

    def editAccess(self):
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Access_css_selector).click()
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Access_css_selector).send_keys(Keys.DOWN)

    def addAccess(self):
        self.driver.find_element(By.CSS_SELECTOR, self.drp_Access_css_selector).send_keys(Keys.ENTER)

    def addButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_Add_css_selector).click()

    def removeButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_Remove_css_selector).click()

    def addBusiness(self,business):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_Business_css_selector).send_keys(business)

    def clickSubmit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_Submit_css_selector).click()

    def okButton(self):
        self.driver.find_element(By.XPATH, self.btn_ok_xpath).click()
