import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.NewFormSearch import NewFormSearch
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

class Test_003_NewFormSearch:
    baseURL = "http://win-6cgsdmg51od:8500/Login/Index"
    username = "cpu"
    password = "Mobinext@123"
    formname = "EQS"

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_NewFormSearch(self,setup):
        self.logger.info("****************Test_003_FormSearch*****************")
        self.logger.info("****************Verifying FormSearch****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        # act_title = self.driver.title
        self.driver.maximize_window()
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
        time.sleep(1)
        self.lp.addNewFormSearch(self.formname)
        time.sleep(1)
        self.lp.downNewFormSearch()
        time.sleep(1)
        self.lp.enterNewFormSearch()
        time.sleep(2)
        act_title = self.driver.title
        if act_title == "IT Production EQ's Access Form":
            assert True
            self.driver.close()
            self.logger.info("****************FormSearch is passed*******(*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_NewFormSearch.png")
            self.driver.close()
            self.logger.error("****************FormSearch is failed****************")
            assert False
        time.sleep(2)
