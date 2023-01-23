import sys
import constants as const
from element import BasePageElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class TextElement(BasePageElement):
    locater = ""
    def __init__(self, value):
        self.locater = value

#Base class to pass webDriver
class BasePage(): 
    def __init__(self, driver):
        self.driver = driver
    

class IndexPage(BasePage):

    def click_login_button(self):
        try:
            login_btn = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((
                    By.XPATH, const.INDEX_LOGIN_BTN_XPATH
                ))
            )
            login_btn.click()
        except Exception as e:
            print("Unable to locate login button on Home Page", file=sys.stderr)
            self.driver.quit()


class LoginPage(BasePage):

    #sets refernces to username and password text fields
    _username_text_element = TextElement(const.LOGIN_USERNAME_XPATH)
    _password_text_element = TextElement(const.LOGIN_PASSWORD_XPATH)

    def set_username(self, value):
        self._username_text_element = value
    
    def set_password(self, value):
        self._password_text_element = value

    def click_submit_button(self):
        try:
            submit_btn = self.driver.find_element(By.XPATH, const.SUBMIT_LOGIN_BTN_XPATH)
            submit_btn.click()
        except Exception as e:
            print("Unable to locate submit button on Login Page", file=sys.stderr)
            self.driver.quit()
    

    def hit_return_key_from_username(self):
        self.driver.find_element(By.XPATH, const.LOGIN_USERNAME_XPATH).send_keys(Keys.ENTER)

    def hit_return_key_from_password(self):
        self.driver.find_element(By.XPATH, const.LOGIN_PASSWORD_XPATH).send_keys(Keys.ENTER)

    def hit_tab_from_username(self):
        self.driver.find_element(By.XPATH, const.LOGIN_USERNAME_XPATH).send_keys(Keys.TAB)

    def hit_tab_from_password(self):
        self.driver.find_element(By.XPATH, const.LOGIN_PASSWORD_XPATH).send_keys(Keys.TAB)

    def refresh_page(self):
        self.driver.refresh()
            

    def is_login_error_displayed(self):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((
                    By.XPATH, const.LOGIN_ERROR_DISPLAY_XPATH
                ))
            )
            return True
        except TimeoutException:
            return False