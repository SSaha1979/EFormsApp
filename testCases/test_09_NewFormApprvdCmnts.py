import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.NewFormSearch import NewFormSearch
from pageObjects.NewFormSubmit import NewFormSubmit
from pageObjects.MyRequest import MyRequest
from pageObjects.NewFormApprvlCmnts import NewFrmApprCmnt
# driver = webdriver.Chrome()
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test_009_ApprvdCmnts:
    baseURL = "http://win-6cgsdmg51od:8500/Login/Index"
    username = "cpu"
    password = "Mobinext@123"
    formname = "EQS"
    empname = "Nidhi"
    empid = "12345"
    logiccard = "76543#$"
    business = "For EQS Access Form Testing purpose"
    # span_MyRequest_id = "myRequestCount"
    span_MyRequest_id = "nav-myrequest-tab"

    logger=LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_MyRequest(self,setup):
        self.logger.info("***************Test_009_FormApprvdCmnts**************")
        self.logger.info("**********Verifying FormApprvdCmnts test*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(2)
        act_title = self.driver.title
        self.driver.maximize_window()
        # # act_title = self.driver.title
        # # self.lp = NewFormSearchPage(self.driver)
        # # self.lp.clickOnNewFormSearchPage()
        # # time.sleep(5)
        # # self.driver.close()
        # if act_title == "Dashboard":
        #     assert True
        # else:
        #     assert False
        self.lp = MyRequest(self.driver)
        time.sleep(2)
        self.lp.clickMyRequest()
        time.sleep(2)
        self.lp.clickMyRequest_view()
        time.sleep(2)
        self.lp.clickMySubmitter_view()
        time.sleep(2)
        self.lp.clickMyApproval_view()
        time.sleep(2)
        self.lp = NewFrmApprCmnt(self.driver)
        time.sleep(2)
        self.lp.clickNewFrmApprCmnt_1()
        time.sleep(2)
        self.lp.clickNewFrmAppr_Ok()
        time.sleep(2)
        self.lp.clickNewFrmApprCmnt_2()
        time.sleep(2)
        self.lp.clickNewFrmAppr_Ok()
        time.sleep(2)
        self.lp.clickNewFrmApprCmnt_3()
        time.sleep(2)
        self.lp.clickNewFrmAppr_Ok()
        time.sleep(2)
        if self.driver.find_element(By.CSS_SELECTOR, "button#cmntBtn.submit-btn.publishBtn"):
            assert True
            self.driver.close()
            self.logger.info("*********NewFormApprvdCmnts test is passed***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_NewFormApprvdCmnts.png")
            self.driver.close()
            self.logger.error("********NewFormApprvdCmnts test is failed***********")
            assert False


