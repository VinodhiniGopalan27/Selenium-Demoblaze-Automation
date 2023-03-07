import unittest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class CartTestCase(unittest.TestCase):
    def setUp(self):
        chromeoptions = webdriver.ChromeOptions()
        chromeoptions.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chromeoptions,
                                       executable_path=r"C:\Users\vinod\Downloads\chromedriver_win32\chromedriver.exe")
        self.url = "https://www.demoblaze.com/"

    def tearDown(self):
        self.driver.quit()

class CartTestCase(unittest.TestCase):
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
        username = self.driver.find_element(By.ID, "loginusername")
        WebDriverWait(self.driver, 5).until(EC.visibility_of(username))
        username.send_keys("Gvino")
        password = self.driver.find_element(By.ID, "loginpassword")
        WebDriverWait(self.driver, 5).until(EC.visibility_of(password))
        password.send_keys("123")
        self.driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))

    def tearDown(self):
        self.driver.quit()

    def test_cancel_order(self):
        driver = self.driver
        cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart")))
        cart.click()
        time.sleep(10)
        driver.find_element("xpath", "//button[contains(text(),'Place Order')]").click()
        name = driver.find_element(By.ID, "name")
        WebDriverWait(driver, 5).until(EC.visibility_of(name))
        name.send_keys("vino")
        credit_cardno = driver.find_element(By.ID, "card")
        WebDriverWait(driver, 5).until(EC.visibility_of(credit_cardno))
        credit_cardno.send_keys("1234")
        year = driver.find_element(By.ID, "year")
        WebDriverWait(driver, 5).until(EC.visibility_of(year))
        year.send_keys("234")
        driver.maximize_window()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//button[text()='Purchase']//preceding-sibling::button")))
        button.click()
        driver.back()
        assert driver.current_url == "https://www.demoblaze.com/"

    def test_place_order(self):
        driver = self.driver
        cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart")))
        cart.click()
        time.sleep(10)
        driver.find_element("xpath", "//button[contains(text(),'Place Order')]").click()
        name = driver.find_element(By.ID, "name")
        WebDriverWait(driver, 5).until(EC.visibility_of(name))
        name.send_keys("vino")
        country = driver.find_element(By.ID, "country")
        WebDriverWait(driver, 5).until(EC.visibility_of(country))
        country.send_keys("abc")
        city = driver.find_element(By.ID, "city")
        WebDriverWait(driver, 5).until(EC.visibility_of(city))
        city.send_keys("X")
        credit_cardno = driver.find_element(By.ID, "card")
        WebDriverWait(driver, 5).until(EC.visibility_of(credit_cardno))
        credit_cardno.send_keys("1234")
        month = driver.find_element(By.ID, "month")
        WebDriverWait(driver, 5).until(EC.visibility_of(month))
        month.send_keys("10")
        year = driver.find_element(By.ID, "year")
        WebDriverWait(driver, 5).until(EC.visibility_of(year))
        year.send_keys("234")
        driver.find_element("xpath", "//button[contains(text(),'Purchase')]").click()
        button = driver.find_element("xpath", "//button[contains(text(),'OK')]")
        button.click()
        assert button.text == "OK"

    def test_placeorder_novalues(self):
        driver = self.driver
        cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart")))
        cart.click()
        driver.find_element("xpath", "//button[contains(text(),'Place Order')]").click()
        name = driver.find_element(By.ID, "name")
        WebDriverWait(driver, 5).until(EC.visibility_of(name))
        name.send_keys("")
        credit_cardno = driver.find_element(By.ID, "card")
        WebDriverWait(driver, 5).until(EC.visibility_of(credit_cardno))
        credit_cardno.send_keys("")
        driver.find_element("xpath", "//button[contains(text(),'Purchase')]").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        message = alert.text
        print(message)
        alert.accept()
        self.assertIn("Please fill out Name and Creditcard.", message)

    def test_placeorder_emptyfields(self):
        driver = self.driver
        cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart")))
        cart.click()
        driver.find_element("xpath", "//button[contains(text(),'Place Order')]").click()
        name = driver.find_element(By.ID, "name")
        WebDriverWait(driver, 5).until(EC.visibility_of(name))
        name.send_keys(" ")
        credit_cardno = driver.find_element(By.ID, "card")
        WebDriverWait(driver, 5).until(EC.visibility_of(credit_cardno))
        credit_cardno.send_keys(" ")
        driver.find_element("xpath", "//button[contains(text(),'Purchase')]").click()
        button = driver.find_element("xpath", "//button[contains(text(),'OK')]")
        button.click()

    def test_placeorder_withnoitems_incart(self):
        driver = self.driver
        cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart")))
        cart.click()
        elements = driver.find_elements(By.LINK_TEXT, "Delete")
        print(len(elements))
        if len(elements) <= 0:
            button = driver.find_element("xpath", "//button[contains(text(),'Place Order')]")
        assert not button.is_enabled(), "The button should not be enabled."

        if __name__ == "__main__":
            unittest.main()


