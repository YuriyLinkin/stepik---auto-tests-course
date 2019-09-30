import math
import time
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/redirect_accept.html")
#action in Window_1
	browser.find_element_by_css_selector("button.trollface.btn.btn-primary").click()

#switch to Window_2
	browser.switch_to.window(browser.window_handles[1])
#action in Window_2
	x = browser.find_element_by_css_selector(".nowrap#input_value").text
	y = calc(x)
	browser.find_element_by_css_selector("#answer.form-control").send_keys(y)
	browser.find_element_by_css_selector("button.btn.btn-primary").click()

finally:
	time.sleep(8)
	browser.quit()


