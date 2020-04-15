class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.welcomeadmin_id= "welcome"
        self.logout_partiallink_text = "Logout"
        self.about_id = "aboutDisplayLink"

    def click_welcomeadmin(self):
        self.driver.find_element_by_id(self.welcomeadmin_id).click()
    def click_logout(self):
        self.driver.find_element_by_partial_link_text("Logout").click()