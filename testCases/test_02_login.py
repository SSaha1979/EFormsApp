import time
import pytest
import random
import string

from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
# driver = webdriver.Chrome()

class Test_002_Login:
    baseURL = "http://win-6cgsdmg51od:8500/Login/Index"
    username = "cpu"
    password = "Mobinext@123"

    # baseURL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUseremail()
    # password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********************Test_002_Login******************")
        self.logger.info("*****************Verifying Login test***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp=LoginPage(self.driver)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)
        act_title=self.driver.title
        # self.lp.spanLogout()
        # time.sleep(2)
        # self.lp.spanLogout()
        # time.sleep(2)
        # self.lp.hrefLogout()
        time.sleep(3)
        if act_title=="Dashboard":
            assert True
            self.driver.close()
            self.logger.info("****************Login test is passed*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("***************Login test is failed*****************")
            assert False


