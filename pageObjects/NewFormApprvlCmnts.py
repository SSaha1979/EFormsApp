from selenium.webdriver.common.by import By

class NewFrmApprCmnt:
    i_NewFrmAppr_xpath_1='//*[@id="comments_1"]'
    i_NewFrmAppr_xpath_2='//*[@id="comments_2"]'
    i_NewFrmAppr_xpath_3='//*[@id="comments_3"]'
    i_NewFrmAppr_css_selector_ok="button#cmntBtn.submit-btn.publishBtn"

    def __init__(self, driver):
        self.driver = driver

    def clickNewFrmApprCmnt_1(self):
        self.driver.find_element(By.XPATH,self.i_NewFrmAppr_xpath_1).click()

    def clickNewFrmApprCmnt_2(self):
        self.driver.find_element(By.XPATH,self.i_NewFrmAppr_xpath_2).click()

    def clickNewFrmApprCmnt_3(self):
        self.driver.find_element(By.XPATH,self.i_NewFrmAppr_xpath_3).click()

    def clickNewFrmAppr_Ok(self):
        self.driver.find_element(By.CSS_SELECTOR,self.i_NewFrmAppr_css_selector_ok).click()
