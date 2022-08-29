from selenium.webdriver.common.by import By


class SearchCustomer:
    email = "SearchEmail"
    search_btn_id = "search-customers"
    firstname = "SearchFirstName"
    lastname = "SearchLastName"
    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver
    def setEmail(self, email):
        self.driver.find_element(By.ID, self.email).clear()
        self.driver.find_element(By.ID, self.email).send_keys(email)
    def setFirstName(self,fname):
        self.driver.find_element(By.ID, self.firstname).clear()
        self.driver.find_element(By.ID, self.firstname).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID, self.lastname).clear()
        self.driver.find_element(By.ID, self.lastname).send_keys(lname)

    def clicksearch(self):
        self.driver.find_element(By.ID, self.search_btn_id).click()

    def get_rows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def get_columns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self,Email):
        flag = False
        for r in range(1, self.get_rows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid==Email:
                flag =True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.get_rows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            Name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if Name.split(' ')[0] == name:
                flag = True
                break
        return flag
