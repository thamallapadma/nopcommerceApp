import pytest
import os
from selenium import webdriver
from pathlib import *
from Utilities.commonhelper import CommonHelper

@pytest.fixture()
def setup(browser):
    global driver
    cm=CommonHelper()
    logger = cm.get_logger()
    if browser == 'chrome':
        root_path = str(Path(__file__).parent.parent)
        driver = webdriver.Chrome(os.path.join(root_path,"Drivers","chromedriver"))
        logger.info("launching chrome browser")
    elif browser == 'firefox':
        root_path = str(Path(__file__).parent.parent)
        driver = webdriver.Firefox(executable_path=os.path.join(root_path, "Drivers", "geckodriver"))
        logger.info("launching firefox browser")
    else:
        root_path = str(Path(__file__).parent.parent)
        driver = webdriver.Chrome(os.path.join(root_path, "Drivers", "chromedriver"))
        logger.info("launching chrome browser")

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['project Name'] = 'nop commerce'
    config._metadata['module Name'] = 'Customers'
    config._metadata['Tester'] = 'Padhu'

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)


