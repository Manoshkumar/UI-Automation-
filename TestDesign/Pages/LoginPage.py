class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id= "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"
        self.forgotpassword_link_id = "forgotPasswordLink"



#Creating the functions/actions/methods for the LoginPage web elements:
    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()
    def click_forgotpassword(self):
        self.driver.find_element_by_id(self.forgotpassword_link_id).click()
