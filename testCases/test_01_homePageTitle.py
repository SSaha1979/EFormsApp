import time
import pytest

from selenium import webdriver
from pageObjects.LoginPage import LoginPage
# driver = webdriver.Chrome()
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_HomePageTitle:
    baseURL = "http://win-6cgsdmg51od:8500/Login/Index"
    # baseURL = ReadConfig.getApplicationURL()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("*******************Test_001_HomePage*****************")
        self.logger.info("******************Verifying HomePage*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(2)
        act_title=self.driver.title
        if act_title=="Login":
            assert True
            self.driver.close()
            self.logger.info("*****************HomePage test is passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("***************HomePage test is failed**************")
            assert False
        time.sleep(2)


