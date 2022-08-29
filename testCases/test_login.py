import os.path
from pathlib import *

import pytest

from pageObject.LoginPage import LoginPage
from Utilities.readproperties import *
from Utilities.commonhelper import CommonHelper
from Utilities.readproperties import ReadConfig


class Test_001_Login:
    common_helper = CommonHelper()
    data = ReadConfig()
    logger = common_helper.get_logger()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("******Start of test_homePageTitle*******")
        time_stamp = str(self.common_helper.time_stamp_generator())
        self.driver = setup
        self.driver.get(self.data.url)
        self.logger.info("Login page is displayed")
        act_title = self.driver.title
        self.logger.info("******End of test_homePageTitle*******")
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.join(self.data.rootpath, "Screenshots", "screenshot"+time_stamp+".png"))
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("******start of test_login*******")
        self.driver = setup
        self.driver.get(self.data.url)
        time_stamp = str(self.common_helper.time_stamp_generator())
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.data.user)
        self.logger.info("Username entered")
        self.lp.enter_password(self.data.password)
        self.logger.info("password entered")
        self.lp.click_login()
        self.logger.info("clicked on login")
        act_title = self.driver.title
        self.logger.info("******End of test_login*******")
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.join(self.data.rootpath, "Screenshots", "screenshot"+time_stamp+".png"))
            self.driver.close()
            assert False

