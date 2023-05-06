import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.NewFormEnquired import NewFrmEnqrLevel
from pageObjects.MyRequest import MyRequest
# driver = webdriver.Chrome()
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

class Test_010_Enquired:
    baseURL = "http://win-6cgsdmg51od:8500/Login/Index"
    username = "mk"
    password = "Mobinext@123"
    comment = "Enquiry Done"

    logger=LogGen.loggen()

    # def test_homePageTitle(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     act_title=self.driver.title
    #     self.driver.close()
    #     if act_title=="Login":
    #         assert True
    #     else:
    #         assert False
    #

    # @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("******************Test_010_Enquire*******************")
        self.logger.info("***************Verifying Enquire test****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(2)
        self.lp=NewFrmEnqrLevel(self.driver)

        self.lp.clickNewFrmEnqr_lvl()
        time.sleep(2)
        self.lp.clickNewFrmEnqr_lvldn()
        time.sleep(2)
        self.lp.addComment_Enqr(self.comment)
        time.sleep(2)
        self.lp.clickEnqrSubmit()
        time.sleep(10)
        if self.driver.find_element(By.ID, "enquireSubmit"):
            assert True
            self.driver.close()
            self.logger.info("****************Enquire test is passed***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Enquire.png")
            self.driver.close()
            self.logger.error("**************Enquire test is failed****************")
            assert False

