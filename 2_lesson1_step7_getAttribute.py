import math
import time
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
 
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/get_attribute.html")
	x = browser.find_element_by_id("treasure").get_attribute("valuex")
	y = calc(x)

	browser.find_element_by_css_selector("input#answer").send_keys(y)
	browser.find_element_by_css_selector("input#robotCheckbox").click()
	browser.find_element_by_css_selector("input#robotsRule").click()
	browser.find_element_by_css_selector("button.btn.btn-default").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(15)
    # закрываем браузер после всех манипуляций
	browser.quit()
