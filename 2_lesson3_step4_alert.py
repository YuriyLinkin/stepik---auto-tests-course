import math
import time
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/alert_accept.html")

	browser.find_element_by_css_selector("button.btn.btn-primary").click()
	browser.switch_to.alert.accept()
	#confirm = browser.switch_to.alert
	#confirm.accept()

	x = browser.find_element_by_css_selector(".nowrap#input_value").text
	y = calc(x)
	browser.find_element_by_css_selector("#answer.form-control").send_keys(y)
	browser.find_element_by_css_selector("button.btn.btn-primary").click()


finally:
	time.sleep(8)
	browser.quit()


