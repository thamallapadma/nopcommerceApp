import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    customers_main_tab_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    customers_sub_tab_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    add_new_customer_link_xpath = "//a[@href='/Admin/Customer/Create']"
    email_textbox_xpath = "Email"
    password_textbox_xpath = "Password"
    firstnam_textbox_xpath = "FirstName"
    lastname_textbox_xpath = "LastName"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']//input[@class='k-input']"
    lstitemAdministators_xpath = "//li[contains(text(),'Administrators')]"
    lsitemRegistred_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmrgvendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompanyname_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_customermenu(self):
        self.driver.find_element(By.XPATH, self.customers_main_tab_xpath).click()

    def click_on_customermenuitem(self):
        self.driver.find_element(By.XPATH, self.customers_sub_tab_xpath).click()

    def click_on_addnewbutton(self):
        self.driver.find_element(By.XPATH, self.add_new_customer_link_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_textbox_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_xpath).send_keys(password)

    def enter_customroles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lsitemRegistred_xpath)
        elif role == 'Administrator':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministators_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lsitemRegistred_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmrgvendor_xpath))
        drp.select_by_visible_text(value)
    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def enter_firstname(self, fname):
        self.driver.find_element(By.ID, self.firstnam_textbox_xpath).send_keys(fname)

    def enter_lastname(self, lname):
        self.driver.find_element(By.ID, self.lastname_textbox_xpath).send_keys(lname)

    def enter_DOB(self, DOB):
        self.driver.find_element(By.XPATH, self.txtDOB_xpath).send_keys(DOB)

    def enter_company(self, Comapny):
        self.driver.find_element(By.XPATH, self.txtCompanyname_xpath).send_keys(Comapny)

    def setAdminContent(self, Content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(Content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()


