from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    username_textbox_id = "Email"
    password_textbox_id = "Password"
    login_button_xpath = "//button[@class='button-1 login-button']"
    logout_link_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linktext).click()
