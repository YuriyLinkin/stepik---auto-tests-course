import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	#browser.implicitly_wait(1)
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

#action_1
	price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
	button = WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.ID, "book"))).click()

#action_2
	x = browser.find_element_by_css_selector(".nowrap#input_value").text
	y = calc(x)
	browser.find_element_by_css_selector("#answer.form-control").send_keys(y)
	browser.find_element_by_id("solve").click()

finally:
	time.sleep(15)
	browser.quit()


