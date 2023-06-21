from selenium.webdriver.common.by import By

class NewFrmApprLevel:
    i_NewFrmAppr_xpath='//*[@id="EQSA6540"]/td[7]/div/button/i'
    i_NewFrmAppr_xpath_done='//*[@id="btnApprove"]/label'
    txt_Approve_xpath='//*[@id="comment-approve"]'
    btn_ApprSubmit_id="approveSubmit"


    def __init__(self, driver):
        self.driver = driver

    def clickNewFrmAppr_lvl(self):
        self.driver.find_element(By.XPATH,self.i_NewFrmAppr_xpath).click()

    def clickNewFrmAppr_lvldn(self):
        self.driver.find_element(By.XPATH,self.i_NewFrmAppr_xpath_done).click()

    def addComment_Appr(self,comment):
        self.driver.find_element(By.XPATH,self.txt_Approve_xpath).click()
        self.driver.find_element(By.XPATH,self.txt_Approve_xpath).send_keys(comment)

    def clickApprvSubmit(self):
        self.driver.find_element(By.ID,self.btn_ApprSubmit_id).click()

