import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.NewFormSearch import NewFormSearch
from pageObjects.NewFormSubmit import NewFormSubmit
from pageObjects.MyRequest import MyRequest
from utilities.customLogger import LogGen
# driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

class Test_010_NewFormSubmit1:
    baseURL = "http://win-6cgsdmg51od:8500/Login/Index"
    username = "cpu"
    password = "Mobinext@123"
    formname = "EQS"
    empname = "Nidhi"
    empid = "12345"
    logiccard = "76543#$"
    business = "For EQS Access Form Testing purpose"

    logger=LogGen.loggen()

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_NewFormSubmit(self,setup):
        self.logger.info("*****************Test_010_FormSubmit*****************")
        self.logger.info("****************Verifying FormSubmit*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(2)
        act_title = self.driver.title
        self.driver.maximize_window()
        # act_title = self.driver.title
        # self.lp = NewFormSearchPage(self.driver)
        # self.lp.clickOnNewFormSearchPage()
        # time.sleep(5)
        # self.driver.close()
        # if act_title == "Dashboard":
        #     assert True
        # else:
        #     assert False
        self.lp = NewFormSearch(self.driver)
        self.lp.editNewFormSearch()
        time.sleep(2)
        self.lp.addNewFormSearch(self.formname)
        time.sleep(2)
        self.lp.downNewFormSearch()
        time.sleep(2)
        self.lp.enterNewFormSearch()
        time.sleep(2)
        self.lp = NewFormSubmit(self.driver)
        time.sleep(2)
        self.lp.editEmpDesign()
        time.sleep(2)
        self.lp.addEmpDesign()
        time.sleep(2)
        self.lp.editEmpLocation()
        time.sleep(2)
        self.lp.addEmpLocation()
        time.sleep(2)
        self.lp.editEmpSubmission()
        time.sleep(2)
        self.lp.addEmpSubmission()
        time.sleep(2)
        self.lp.clickRequest()
        time.sleep(2)
        self.lp.addEmpName(self.empname)
        time.sleep(2)
        self.lp.addEmpID(self.empid)
        time.sleep(2)
        self.lp.addLogicCard(self.logiccard)
        time.sleep(2)
        self.lp.editStnName()
        time.sleep(2)
        self.lp.addStnName()
        time.sleep(2)
        self.lp.editShop()
        time.sleep(2)
        self.lp.addShop()
        time.sleep(2)
        self.lp.editAccess()
        time.sleep(2)
        self.lp.addAccess()
        time.sleep(2)
        self.lp.addButton()
        time.sleep(2)
        self.lp.removeButton()
        time.sleep(2)
        self.lp.addBusiness(self.business)
        time.sleep(2)
        self.lp.clickSubmit()
        if self.driver.find_element(By.CSS_SELECTOR, "button#btnSubmit.btn.btn-primary.btn-sm.submit-btn"):
            assert True
            self.logger.info("*****************FormSubmit is passed****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_NewFormSubmit.png")
            self.driver.close()
            self.logger.error("*****************FormSubmit is failed***************")
            assert False
        time.sleep(20)
        self.lp.okButton()
        time.sleep(5)


