import unittest
import page
import constants as const
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class TestLoginVerification(unittest.TestCase):

    def setUp(self):
        op = webdriver.ChromeOptions()
        op.add_experimental_option('excludeSwitches', ['enable=logging'])
        self.driver = webdriver.Chrome(service=Service(const.CHROME_WEBDRIVER_PATH), options=op)
        self.driver.get(const.HUDL_URL)
        self.driver.maximize_window()
        self.go_to_login_page()

    def go_to_login_page(self):
        self.mainPage = page.IndexPage(self.driver)
        self.mainPage.click_login_button()
        self.loginPage = page.LoginPage(self.driver)



    def test_valid_username_valid_password(self):
        self.loginPage.set_username(const.USERNAME)
        self.loginPage.set_password(const.PASSWORD)
        self.loginPage.click_submit_button()
        self.assertFalse(self.loginPage.is_login_error_displayed())

    def test_valid_username_invalid_password(self):
        self.loginPage.set_username(const.USERNAME)
        self.loginPage.set_password("Invalid_Password")
        self.loginPage.click_submit_button()
        self.assertTrue(self.loginPage.is_login_error_displayed())

    def test_invalid_username_valid_password(self):
        self.loginPage.set_username("Invalid_Username")
        self.loginPage.set_password(const.PASSWORD)
        self.loginPage.hit_return_key_from_username()
        self.assertTrue(self.loginPage.is_login_error_displayed())

    def test_invalid_username_invalid_password(self):
        self.loginPage.set_username("Invalid_Username")
        self.loginPage.set_password("Invalid_Password")
        self.loginPage.hit_return_key_from_password()
        self.assertTrue(self.loginPage.is_login_error_displayed())



    def test_login_with_return_key(self):
        self.loginPage.set_username(const.USERNAME)
        self.loginPage.set_password(const.PASSWORD)
        self.loginPage.hit_return_key_from_password()
        self.assertFalse(self.loginPage.is_login_error_displayed())



    def test_no_username_or_no_password_and_refresh_page(self):
        self.loginPage.set_username("")
        self.loginPage.set_password(const.PASSWORD)
        self.loginPage.hit_return_key_from_username()
        self.assertTrue(self.loginPage.is_login_error_displayed())

        self.loginPage.refresh_page()
        self.loginPage.set_username(const.USERNAME)
        self.loginPage.set_password("")
        self.loginPage.click_submit_button()
        self.assertTrue(self.loginPage.is_login_error_displayed())

    def test_multiple_refresh_page_and_correct_credentials(self):
        for x in range(6):
            self.loginPage.refresh_page()
        self.loginPage.set_username(const.USERNAME)
        self.loginPage.set_password(const.PASSWORD)
        self.loginPage.click_submit_button()
        self.assertFalse(self.loginPage.is_login_error_displayed())
        
    def test_multiple_refresh_page_and_incorrect_credentials(self):
        for x in range(6):
            self.loginPage.refresh_page()

        self.loginPage.set_username("Invalid_Username")
        self.loginPage.set_password("Invalid_Password")
        self.loginPage.click_submit_button()
        self.assertTrue(self.loginPage.is_login_error_displayed())



    def test_back_and_forth_between_pages_with_valid_credientials(self):
        self.loginPage.set_username(const.USERNAME)
        self.loginPage.set_password("Invalid_Passowrd")
        for x in range(4):
            self.driver.back()
            self.driver.forward()

        self.loginPage.set_username(const.USERNAME)
        self.loginPage.set_password(const.PASSWORD)
        self.loginPage.click_submit_button()
        self.assertFalse(self.loginPage.is_login_error_displayed())



    def test_extraneous_input(self):
        self.loginPage.set_username("!O#*$?!><>?|}+!@)")
        self.loginPage.set_password("@&%#P)@&#<?:}(")
        self.loginPage.click_submit_button()
        self.assertTrue(self.loginPage.is_login_error_displayed())

    def test_character_limit(self):
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ex felis, rhoncus quis tincidunt eget, porttitor a lacus. Cras et"
        self.loginPage.set_username(text)
        self.loginPage.set_password(text)
        self.loginPage.click_submit_button()
        self.assertTrue(self.loginPage.is_login_error_displayed())

    def test_mutliple_attempts(self):
        self.loginPage.set_username("Test_01")
        self.loginPage.set_password("Test_01")
        self.loginPage.hit_return_key_from_username()
        self.assertTrue(self.loginPage.is_login_error_displayed())

        self.loginPage.set_username("Test_02")
        self.loginPage.set_password("Test_02")
        self.loginPage.hit_return_key_from_password()
        self.assertTrue(self.loginPage.is_login_error_displayed())

        self.loginPage.set_username("Test_03")
        self.loginPage.set_password("Test_03")
        self.loginPage.click_submit_button()
        self.assertTrue(self.loginPage.is_login_error_displayed())

        self.loginPage.set_username("Test_04")
        self.loginPage.set_password("Test_04")
        self.loginPage.hit_return_key_from_username()
        self.assertTrue(self.loginPage.is_login_error_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
