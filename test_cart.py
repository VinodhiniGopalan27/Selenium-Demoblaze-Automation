import unittest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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

    def test_add_twoitems_to_cart(self):
        driver = self.driver
        cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart")))
        cart.click()
        time.sleep(10)
        elements = driver.find_elements(By.LINK_TEXT, "Delete")
        print(len(elements))
        driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        clickphone = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Phones")))
        clickphone.click()
        samsungphone = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6")))
        samsungphone.click()
        samsungcart=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart")))
        samsungcart.click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual("Product added.", successMessage)
        driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        clickphone2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Phones")))
        clickphone2.click()
        nokiaphone = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, "Nokia lumia 1520")))
        nokiaphone.click()
        nokiacart=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart")))
        nokiacart.click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert2 = driver.switch_to.alert
        message = alert2.text
        print(message)
        alert.accept()
        self.assertEqual("Product added.", message)
        cart1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart")))
        cart1.click()
        time.sleep(10)
        elements1 = driver.find_elements(By.LINK_TEXT, "Delete")
        print(len(elements1))
        self.assertEqual(len(elements)+2, len(elements1))

    def test_delete_twoitems_from_cart(self):
        driver = self.driver
        cart2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart")))
        cart2.click()
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.LINK_TEXT, "Delete")))
        elements = driver.find_elements(By.LINK_TEXT, "Delete")
        print(len(elements))
        beforedeletecount=len(elements)
        if len(elements) > 0:
            for i in range(2):
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable(elements[i]))
                elements[i].click()
        time.sleep(5)
        elements1 = driver.find_elements(By.LINK_TEXT, "Delete")
        afterdeletecount = len(elements1)
        self.assertEqual(beforedeletecount-2, afterdeletecount)

    def test_addtwo_deleteone_from_cart(self):
        driver = self.driver
        cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart")))
        cart.click()
        time.sleep(5)
        beforecountofcart = driver.find_elements(By.LINK_TEXT, "Delete")
        print(len(beforecountofcart))
        driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        clickphone = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Phones")))
        clickphone.click()
        samsungphone = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6")))
        samsungphone.click()
        samsungcart=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart")))
        samsungcart.click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual("Product added.", successMessage)
        driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        clickphone2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Phones")))
        clickphone2.click()
        nokiaphone = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, "Nokia lumia 1520")))
        nokiaphone.click()
        nokiacart=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart")))
        nokiacart.click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert2 = driver.switch_to.alert
        message = alert2.text
        print(message)
        alert.accept()
        self.assertEqual("Product added.", message)
        cart1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart")))
        cart1.click()
        time.sleep(10)
        deleteitem = driver.find_elements(By.LINK_TEXT, "Delete")
        deleteitem[0].click()
        time.sleep(10)
        aftercountofcart = driver.find_elements(By.LINK_TEXT, "Delete")
        print(len(aftercountofcart))
        self.assertEqual(len(beforecountofcart)+1, len(aftercountofcart))
        print("Total No of items in the Cart:", len(aftercountofcart))

    def test_totalno_of_items(self):
        driver = self.driver
        cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart")))
        cart.click()
        time.sleep(10)
        noofitemsinthecart = driver.find_elements(By.LINK_TEXT, "Delete")
        self.assertGreaterEqual(len(noofitemsinthecart),0)
        print("Total No of items in the Shopping Cart:",  len(noofitemsinthecart))


    if __name__ == "__main__":
        unittest.main()




