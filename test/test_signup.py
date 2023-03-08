import unittest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSignup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='drivers/chromedriver')
        self.url = "https://www.demoblaze.com/"

    def tearDown(self):
        self.driver.quit()

    def test_successful_signup(self):
        driver = self.driver
        driver.get(self.url)
        signup = driver.find_element(By.ID, "signin2")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(signup))
        signup.click()
        username = driver.find_element(By.ID, "sign-username")
        WebDriverWait(driver, 5).until(EC.visibility_of(username))
        username.send_keys("Gvino2")
        password = driver.find_element(By.ID, "sign-password")
        WebDriverWait(driver, 5).until(EC.visibility_of(password))
        password.send_keys("123")
        driver.find_element("xpath", "//button[contains(text(),'Sign up')]").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        message = alert.text
        print(message)
        alert.accept()
        self.assertIn("Sign up successful.", message)

    def test_emptyfields(self):
        driver = self.driver
        driver.get(self.url)
        signup = driver.find_element(By.ID, "signin2")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(signup))
        signup.click()
        username = driver.find_element(By.ID, "sign-username")
        WebDriverWait(driver, 5).until(EC.visibility_of(username))
        username.send_keys("")
        password = driver.find_element(By.ID, "sign-password")
        WebDriverWait(driver, 5).until(EC.visibility_of(password))
        password.send_keys("")
        driver.find_element("xpath", "//button[contains(text(),'Sign up')]").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        message = alert.text
        print(message)
        self.assertIn("Please fill out Username and Password.", message)

    def test_whitespacefields(self):
        driver = self.driver
        driver.get(self.url)
        signup = driver.find_element(By.ID, "signin2")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(signup))
        signup.click()
        username = driver.find_element(By.ID, "sign-username")
        WebDriverWait(driver, 5).until(EC.visibility_of(username))
        username.send_keys(" ")
        password = driver.find_element(By.ID, "sign-password")
        WebDriverWait(driver, 5).until(EC.visibility_of(password))
        password.send_keys(" ")
        driver.find_element("xpath", "//button[contains(text(),'Sign up')]").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        message = alert.text
        print(message)
        alert.accept()
        self.assertIn("Please fill out Username and Password.", message)

    def test_Username_already_exists(self):
        driver = self.driver
        driver.get(self.url)
        signup = driver.find_element(By.ID, "signin2")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(signup))
        signup.click()
        username = driver.find_element(By.ID, "sign-username")
        WebDriverWait(driver, 5).until(EC.visibility_of(username))
        username.send_keys("Gvino")
        password = driver.find_element(By.ID, "sign-password")
        WebDriverWait(driver, 5).until(EC.visibility_of(password))
        password.send_keys("123")
        driver.find_element("xpath", "//button[contains(text(),'Sign up')]").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        message = alert.text
        print(message)
        alert.accept()
        self.assertIn("This user already exist.", message)

if __name__ == "__main__":
    unittest.main()
