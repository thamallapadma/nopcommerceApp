import time

import pytest
from selenium.webdriver.common.by import By

from pageObject.searchCustomer import SearchCustomer
from pageObject.LoginPage import LoginPage
from pageObject.AddCustomer import AddCustomer
from Utilities.readproperties import ReadConfig
from Utilities.commonhelper import CommonHelper


class Test_004_SearchCustomer:
    common_helper = CommonHelper()
    data = ReadConfig()
    logger = common_helper.get_logger()
    randgen = common_helper.random_generator()

    @pytest.mark.regression
    def test_search_customer_by_email(self,setup):
        self.logger.info("******start of test_addCustomer*******")
        self.driver = setup
        self.driver.get(self.data.url)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.data.user)
        self.lp.enter_password(self.data.password)
        self.lp.click_login()
        self.logger.info("*****Login successful*******")
        self.logger.info("-------Starting search CUSTOMER TEST------")
        self.addcustom = AddCustomer(self.driver)
        self.addcustom.click_customermenu()
        self.addcustom.click_on_customermenuitem()

        self.logger.info("searching customer by email")
        searchcust = SearchCustomer(self.driver)
        if self.driver.find_element(By.ID, "SearchEmail").is_displayed() is False:
            self.driver.find_element(By.XPATH, "//div[@class='row search-row ']").click()
        time.sleep(2)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clicksearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("Completed")
        self.driver.close()