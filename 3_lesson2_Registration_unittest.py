from selenium import webdriver
import unittest

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_success_registration(self):
        browser = self.browser

        browser.get("http://suninjuly.github.io/registration1.html")
        browser.find_element_by_css_selector('div.first_block .form-control.first').send_keys("FN-Success!")
        browser.find_element_by_css_selector('div.first_block .form-control.second').send_keys("LN-Success!")
        browser.find_element_by_css_selector('div.first_block .form-control.third').send_keys("Success@email.com")
        browser.find_element_by_css_selector("button.btn").click()
        welcome_text = browser.find_element_by_tag_name("h1").text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_fail_registration(self):
        browser = self.browser

        browser.get("http://suninjuly.github.io/registration2.html")
        browser.find_element_by_css_selector('div.first_block .form-control.first').send_keys("FN-Success!")
        browser.find_element_by_css_selector('div.first_block .form-control.second').send_keys("LN-Success!")
        browser.find_element_by_css_selector('div.first_block .form-control.third').send_keys("Success@email.com")
        browser.find_element_by_css_selector("button.btn").click()
        welcome_text = browser.find_element_by_tag_name("h1").text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()

