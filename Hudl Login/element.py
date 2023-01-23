import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#sets and gets the texts feilds for both username and password in login page
class BasePageElement():

    def __set__(self, obj, value):
        try:
            driver = obj.driver
            WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((
                        By.XPATH, self.locater
                    ))
                )
            driver.find_element(By.XPATH, self.locater).clear()
            driver.find_element(By.XPATH, self.locater).send_keys(value)
        except Exception as e:
            print("Unable to locate Username or Password on Login Page", file=sys.stderr)
            self.driver.quit()

    def __get__(self, obj, owner):
        try:
            driver = obj.driver
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element(By.XPATH, self.locater)
            )
            element = driver.find_element(By.XPATH, self.locater)
            return element.get_attribute("value")
        except Exception as e:
            print("Unable to locate Username or Password on Login Page", file=sys.stderr)
            self.driver.quit()