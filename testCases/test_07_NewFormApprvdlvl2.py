import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.NewFormApproved import NewFrmApprLevel
from pageObjects.MyRequest import MyRequest
# driver = webdriver.Chrome()
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test_007_ApproveLVL2:
    baseURL = "http://win-6cgsdmg51od:8500/Login/Index"
    username = "neha"
    password = "Mobinext@123"
    comment = "Approval Level 2 done."

    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***************Test_007_Approval_LVL2***************")
        self.logger.info("************Verifying Approval_LVL2 test************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(2)
        self.lp=NewFrmApprLevel(self.driver)
        self.lp.clickNewFrmAppr_lvl()
        time.sleep(2)
        self.lp.clickNewFrmAppr_lvldn()
        time.sleep(2)
        self.lp.addComment_Appr(self.comment)
        time.sleep(2)
        self.lp.clickApprvSubmit()
        time.sleep(15)
        if self.driver.find_element(By.ID, "approveSubmit"):
            assert True
            self.driver.close()
            self.logger.info("************Approval_LVL2 test is passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_NewFormApprvdlvl2.png")
            self.driver.close()
            self.logger.error("************Approval_LVL2 test is failed************")
            assert False
