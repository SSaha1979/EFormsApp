import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.NewFormRejected import NewFrmRejectLvl
from pageObjects.MyRequest import MyRequest
# driver = webdriver.Chrome()
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

class Test_011_Rejected:
    baseURL = "http://win-6cgsdmg51od:8500/Login/Index"
    username = "mk"
    password = "Mobinext@123"
    comment = "It is for Automation Testing"

    logger=LogGen.loggen()

    # @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("******************Test_011_Reject********************")
        self.logger.info("****************Verifying Reject test****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(2)
        self.lp=NewFrmRejectLvl(self.driver)
        self.lp.clickNewFrmRjct_lvl()
        time.sleep(2)
        self.lp.clickNewFrmRjct_lvldn()
        time.sleep(2)
        self.lp.addComment_Rjct(self.comment)
        time.sleep(2)
        self.lp.clickRjctSubmit()
        time.sleep(10)
        if self.driver.find_element(By.ID, "rejectSubmit"):
            assert True
            self.driver.close()
            self.logger.info("****************Reject test is passed****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Reject.png")
            self.driver.close()
            self.logger.error("***************Reject test is failed****************")
            assert False


