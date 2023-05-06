# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class MyRequest:
    span_MyRequest_id = "nav-myrequest-tab"
    i_MyRequest_xpath='//*[@id="requestTable"]/tbody/tr[1]/td[7]/div/button[1]/i'
    submitter_xpath='//*[@id="headingOne"]/h5'
    approval_xpath='//*[@id="headingFour"]/h5'

    def __init__(self, driver):
        self.driver = driver

    def clickMyRequest(self):
        self.driver.find_element(By.ID,self.span_MyRequest_id).click()

    def clickMyRequest_view(self):
        self.driver.find_element(By.XPATH,self.i_MyRequest_xpath).click()

    def clickMySubmitter_view(self):
        self.driver.find_element(By.XPATH,self.submitter_xpath).click()

    def clickMyApproval_view(self):
        self.driver.find_element(By.XPATH,self.approval_xpath).click()


