import pytest
import time

from selenium.webdriver.common.by import By

from pageObject.LoginPage import LoginPage
from pageObject.AddCustomer import AddCustomer
from Utilities.readproperties import ReadConfig
from Utilities.commonhelper import CommonHelper
import string
import random

class Test_003_AddCustomer:
    common_helper = CommonHelper()
    data = ReadConfig()
    logger = common_helper.get_logger()
    randgen = common_helper.random_generator()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("******start of test_addCustomer*******")
        self.driver = setup
        self.driver.get(self.data.url)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.data.user)
        self.lp.enter_password(self.data.password)
        self.lp.click_login()
        self.logger.info("*****Login successful*******")
        self.logger.info("-------Starting ADD CUSTOMER TEST------")
        self.addcustom = AddCustomer(self.driver)
        self.addcustom.click_customermenu()
        self.addcustom.click_on_customermenuitem()
        self.addcustom.click_on_addnewbutton()
        self.logger.info("------Providing customer info-----")
        self.email = self.randgen +"@gmail.com"
        self.addcustom.enter_email(self.email)
        self.addcustom.enter_password("admin123")
        time.sleep(2)
        self.addcustom.enter_firstname("Daisy")
        self.addcustom.enter_lastname("twinkle")
        self.addcustom.setGender("Female")
        self.addcustom.enter_DOB("03/22/2000")
        self.addcustom.enter_company("xyz")
        time.sleep(2)
        self.addcustom.enter_customroles("Guests")
        self.addcustom.setManagerOfVendor("Vendor 2")


        self.addcustom.setAdminContent("This is for testing.....")
        self.addcustom.clickOnSave()
        self.logger.info("------saving customer info------")
        self.logger.info("------ADD customer validation started-----")
        self.msg =self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("Add customer test passed")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots"+"sc.png")
            self.logger.error("-----ADD CUSTOMER TEST FAILED-----")
            self.driver.close()
            assert False




