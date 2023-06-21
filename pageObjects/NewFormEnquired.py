from selenium.webdriver.common.by import By

class NewFrmEnqrLevel:
    i_NewFrmEnqr_xpath='//*[@id="EQSA6535"]/td[7]/div/button/i'
    i_NewFrmEnqr_xpath_done='//*[@id="btnEnquire"]/label'
    txt_Enquire_xpath='//*[@id="comment-enquire"]'
    btn_EnqrSubmit_id="enquireSubmit"


    def __init__(self, driver):
        self.driver = driver

    def clickNewFrmEnqr_lvl(self):
        self.driver.find_element(By.XPATH,self.i_NewFrmEnqr_xpath).click()

    def clickNewFrmEnqr_lvldn(self):
        self.driver.find_element(By.XPATH,self.i_NewFrmEnqr_xpath_done).click()

    def addComment_Enqr(self,comment):
        self.driver.find_element(By.XPATH,self.txt_Enquire_xpath).click()
        self.driver.find_element(By.XPATH,self.txt_Enquire_xpath).send_keys(comment)

    def clickEnqrSubmit(self):
        self.driver.find_element(By.ID,self.btn_EnqrSubmit_id).click()

