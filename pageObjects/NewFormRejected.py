from selenium.webdriver.common.by import By

class NewFrmRejectLvl:
    i_NewFrmReject_xpath='//*[@id="EQSA6137"]/td[7]/div/button/i'
    i_NewFrmReject_xpath_done='//*[@id="btnReject"]/label'
    txt_Reject_xpath='//*[@id="comment-reject"]'
    btn_RjctSubmit_id="rejectSubmit"



    def __init__(self, driver):
        self.driver = driver

    def clickNewFrmRjct_lvl(self):
        self.driver.find_element(By.XPATH,self.i_NewFrmReject_xpath).click()

    def clickNewFrmRjct_lvldn(self):
        self.driver.find_element(By.XPATH,self.i_NewFrmReject_xpath_done).click()

    def addComment_Rjct(self,comment):
        self.driver.find_element(By.XPATH,self.txt_Reject_xpath).click()
        self.driver.find_element(By.XPATH,self.txt_Reject_xpath).send_keys(comment)

    def clickRjctSubmit(self):
        self.driver.find_element(By.ID,self.btn_RjctSubmit_id).click()

