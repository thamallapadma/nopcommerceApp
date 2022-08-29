import os.path
import time
from pathlib import *

import pytest

from pageObject.LoginPage import LoginPage
from Utilities.readproperties import *
from Utilities.commonhelper import CommonHelper
from Utilities.readproperties import ReadConfig
from Utilities import excelutilities

class Test_002_DDT_Login:
    common_helper = CommonHelper()
    data = ReadConfig()
    logger = common_helper.get_logger()
    path =".//TestData/credentialsHF.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("----------Test_002_DDT_Login-------")
        self.logger.info("******start of test_login_ddt*******")
        self.driver = setup
        self.driver.get(self.data.url)
        time_stamp = str(self.common_helper.time_stamp_generator())
        self.lp = LoginPage(self.driver)
        self.rows = excelutilities.getRowCount(self.path, 'Sheet1')
        self.logger.info(self.rows)
        lst_status = []
        for r in range(2, self.rows+1):
            self.user = excelutilities.readData(self.path, 'Sheet1', r, 1)
            self.password = excelutilities.readData(self.path, 'Sheet1', r, 2)
            self.status = excelutilities.readData(self.path, 'Sheet1', r, 3)
            self.lp.enter_username(self.user)
            self.logger.info("Username entered")
            self.lp.enter_password(self.data.password)
            self.logger.info("password entered")
            self.lp.click_login()
            self.logger.info("clicked on login")
            time.sleep(5)
            act_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"
            self.logger.info("******End of test_login*******")
            if act_title == expected_title:
                if self.status == "pass":
                    self.logger.info("---passed---")
                    self.lp.click_logout()
                    lst_status.append("pass")
                elif self.status == "fail":
                    self.logger.info("----failed----")
                    self.lp.click_logout()
                    lst_status.append("fail")
            elif act_title != expected_title:
                if self.status == "pass":
                    self.logger.info("---passed---")
                    lst_status.append("pass")
                elif self.status == "fail":
                    self.logger.info("----failed----")
                    lst_status.append("fail")
        if "Fail" not in lst_status:
            self.logger.info("Login DDT test passed...")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test passed...")
            self.driver.close()
            assert False

