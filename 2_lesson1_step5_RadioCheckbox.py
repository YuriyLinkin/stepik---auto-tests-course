import math
import time
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
 
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/math.html")
	x_element = browser.find_element_by_css_selector(".nowrap#input_value")
	x = x_element.text
	y = calc(x)
	browser.find_element_by_css_selector("#answer.form-control").send_keys(y)
	browser.find_element_by_css_selector("[for='robotCheckbox']").click()
	browser.find_element_by_css_selector("[for='robotsRule']").click()
	browser.find_element_by_css_selector("button.btn.btn-default").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(15)
    # закрываем браузер после всех манипуляций
	browser.quit()
