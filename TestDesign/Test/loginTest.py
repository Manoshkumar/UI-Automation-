from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from TestDesign.Pages.LoginPage import LoginPage
from TestDesign.Pages.HomePage import HomePage

class LoginTest(unittest.TestCase):
    valid_username = "Admin"
    invalid_username = "Manosh"
    valid_password = "admin123"
    invalid_password = "Manosh123"

    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/Nithin/PycharmProjects/OrangeHRM/Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")

# Testcase-1==> Login with invalid password
    def test_01_login_invalid_password(self):
        login = LoginPage(self.driver)
        login.enter_username(self.valid_username)
        login.enter_password(self.invalid_password)
        login.click_login()
        time.sleep(10)
        error = self.driver.find_element_by_id("spanMessage").text
        assert error == "Invalid credentials"
        print("Test cases-1 passed")
# Testcase-2==> Login with invalid username
    def test_02_login_invalid_Username(self):
        login = LoginPage(self.driver)
        login.enter_username(self.invalid_username)
        login.enter_password(self.valid_password)
        login.click_login()
        time.sleep(10)
        error = self.driver.find_element_by_id("spanMessage").text
        assert error == "Invalid credentials"
        print("Test cases-2 passed")
# Testcase-3==> Login with valid username and password
    def test_03_login_success(self):
        login = LoginPage(self.driver)
        login.enter_username(self.valid_username)
        login.enter_password(self.valid_password)
        login.click_login()
        time.sleep(10)
        success = self.driver.find_element_by_id("welcome").text
        assert success == "Welcome Admin"
        print("Test cases-3 passed")
# Testcase-4==> Logout from the account
    def test_04_logout(self):
        login = LoginPage(self.driver)
        login.enter_username(self.valid_username)
        login.enter_password(self.valid_password)
        login.click_login()
        time.sleep(5)
        logout = HomePage(self.driver)
        logout.click_welcomeadmin()
        logout.click_logout()
        time.sleep(10)
        logintext = self.driver.find_element_by_id("logInPanelHeading").text
        assert logintext == "LOGIN Panel"
        print("Test cases-4 passed")


    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Nithin/PycharmProjects/OrangeHRM/Reports'))