import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Amazon(unittest.TestCase):
    @classmethod
    def setUp(cls):
     # create a new Chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
    # navigate to the Amazon home page
        cls.driver.get("https://www.amazon.ca/")

    def test_for_step_one(self):
        time.sleep(2)
        SignedStaus = self.driver.find_element_by_id("nav-link-yourAccount").text
        # verify user is not signed in
        if "Hello. Sign in" not in SignedStaus:
            raise Exception("User already signed in")
        else:
            print "Step 1 - User has not logged In"

    def test_for_step_two(self):
        self.driver.find_element_by_id("nav-link-yourAccount").click()
        time.sleep(2)
        self.Email = self.driver.find_element_by_id("ap_email")
        self.Email.send_keys("rajagiriyakotte1234@gmail.com")
        self.driver.find_element_by_id("continue").click()
        time.sleep(2)
        self.Email = self.driver.find_element_by_id("ap_password")
        self.Email.send_keys("W0rkopolis")
        self.driver.find_element_by_id("signInSubmit").click()
        time.sleep(2)
        SignedStaus = self.driver.find_element_by_id("nav-link-yourAccount").text
        # verify user is signed in
        if "Sim" not in SignedStaus:
            raise Exception("User Sign In did not work")
        else:
            print "Step 2 - User has successfully logged in as Sim Test"

    def test_for_step_three(self):
        self.searcbar = self.driver.find_element_by_id("twotabsearchtextbox")
        self.searcbar.send_keys("memory card")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(2)
        ResultCount = self.driver.find_element_by_id("s-result-count").text
        # verify search returns results
        if "results" and "memory" not in ResultCount:
            raise Exception("Search did not return any results")
        else:
            print "Step 3 - Amazon search was successful"

    def test_for_step_four(self):
        self.searcbar = self.driver.find_element_by_id("twotabsearchtextbox")
        self.searcbar.send_keys("[alpja]")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(2)
        NoResultTitle = self.driver.find_element_by_id("noResultsTitle").text
        # verify message indicating no search results were returned is shown
        if "Your search " and "[alpja]" and " did not match any products." not in NoResultTitle:
            raise Exception("No match text not displayed")
        else:
            print "Step 4 - Notice shown for Your search '[alpja]' did not match any products"

    def test_for_step_five(self):
        self.searcbar = self.driver.find_element_by_id("twotabsearchtextbox")
        self.searcbar.send_keys("memory card")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//h2[@data-attribute='Sandisk Ultra 32GB Class 10 SDHC UHS-I Memory Card Up to 80MB, Grey/Black (SDSDUNC-032G-GN6IN)']").click()
        time.sleep(2)
        self.driver.find_element_by_id("add-to-cart-button").click()
        time.sleep(2)
        self.driver.find_element_by_id("hlb-ptc-btn-native").click()
        self.Email = self.driver.find_element_by_id("ap_email")
        self.Email.send_keys("rajagiriyakotte1234@gmail.com")
        self.driver.find_element_by_id("continue").click()
        time.sleep(2)
        self.Email = self.driver.find_element_by_id("ap_password")
        self.Email.send_keys("W0rkopolis")
        self.driver.find_element_by_id("signInSubmit").click()
        time.sleep(3)
        PageUrl = self.driver.current_url
        # verify from the page url that the user is directed to the create shipping address page
        if "buy/addressselect" not in PageUrl:
            raise Exception("Shipping address page not displayed")
        else:
            print "Step 5 - Logged in user is taken to enter shipping address page after adding to cart"

    def tearDown(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)