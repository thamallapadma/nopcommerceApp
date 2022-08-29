import time

import pytest

from pageObject.searchCustomer import SearchCustomer
from pageObject.LoginPage import LoginPage
from pageObject.AddCustomer import AddCustomer
from Utilities.readproperties import ReadConfig
from Utilities.commonhelper import CommonHelper


class Test_005_SearchCustomer:
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
        searchcust.setFirstName("Victoria")
        searchcust.clicksearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria")
        assert True == status
        self.logger.info("Completed")
        self.driver.close()