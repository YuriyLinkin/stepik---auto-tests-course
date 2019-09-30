import math
import time
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/execute_script.html")
	
	x = browser.find_element_by_css_selector(".nowrap#input_value").text
	y = calc(x)
	browser.find_element_by_css_selector("#answer.form-control").send_keys(y)
	browser.find_element_by_css_selector("[for='robotCheckbox']").click()

	browser.execute_script("window.scrollBy(0, 110);")

	browser.find_element_by_css_selector("[for='robotsRule']").click()
	browser.find_element_by_css_selector("button.btn.btn-primary").click()

	#browser.execute_script("document.title='Script executing';")
	#browser.execute_script("alert('Robots at work');")
	#browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(12)
    # закрываем браузер после всех манипуляций
	browser.quit()
