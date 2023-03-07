import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginTestCase(unittest.TestCase):
    def setUp(self):
        chromeoptions = webdriver.ChromeOptions()
        chromeoptions.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chromeoptions,
                                       executable_path=r"C:\Users\vinod\Downloads\chromedriver_win32\chromedriver.exe")
        self.url = "https://www.demoblaze.com/"
        self.driver.get(self.url)
        login = self.driver.find_element(By.ID, "login2")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(login))
        login.click()

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        driver = self.driver
        username = driver.find_element(By.ID, "loginusername")
        WebDriverWait(driver, 5).until(EC.visibility_of(username))
        username.send_keys("Gvino")
        password = driver.find_element(By.ID, "loginpassword")
        WebDriverWait(driver, 5).until(EC.visibility_of(password))
        password.send_keys("123")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
        usermessage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nameofuser")))
        print(usermessage.is_displayed())
        message = usermessage.text
        self.assertIn("Welcome Gvino", message)

    def test_emptyfields(self):
        driver = self.driver
        username = driver.find_element(By.ID, "loginusername")
        WebDriverWait(driver, 5).until(EC.visibility_of(username))
        username.send_keys("")
        password = driver.find_element(By.ID, "loginpassword")
        WebDriverWait(driver, 5).until(EC.visibility_of(password))
        password.send_keys("")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        message = alert.text
        print(message)
        alert.accept()
        self.assertIn("Please fill out Username and Password.", message)

    def test_invalidusername(self):
        driver = self.driver
        username = driver.find_element(By.ID, "loginusername")
        WebDriverWait(driver, 5).until(EC.visibility_of(username))
        username.send_keys("aadvik")
        password = driver.find_element(By.ID, "loginpassword")
        WebDriverWait(driver, 5).until(EC.visibility_of(password))
        password.send_keys("123")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        message = alert.text
        print(message)
        alert.accept()
        self.assertIn("User does not exist.", message)

    def test_invalidpassword(self):
        driver = self.driver
        username = driver.find_element(By.ID, "loginusername")
        WebDriverWait(driver, 5).until(EC.visibility_of(username))
        username.send_keys("Gvino")
        password = driver.find_element(By.ID, "loginpassword")
        WebDriverWait(driver, 5).until(EC.visibility_of(password))
        password.send_keys("1234")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        message = alert.text
        print(message)
        alert.accept()
        self.assertIn("Wrong password.", message)

    def test_successful_logout(self):
        driver = self.driver
        username = driver.find_element(By.ID, "loginusername")
        WebDriverWait(driver, 5).until(EC.visibility_of(username))
        username.send_keys("Gvino")
        password = driver.find_element(By.ID, "loginpassword")
        WebDriverWait(driver, 5).until(EC.visibility_of(password))
        password.send_keys("123")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nameofuser")))
        driver.find_element(By.LINK_TEXT, "Log out").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log in")))
        usermessage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nameofuser")))
        self.assertFalse(usermessage.is_displayed())

if __name__ == "__main__":
    unittest.main()
