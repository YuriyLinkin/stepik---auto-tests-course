import os 
import time
from selenium import webdriver

try:
 
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/file_input.html")

	browser.find_element_by_name("firstname").send_keys("FirstN")
	browser.find_element_by_name("lastname").send_keys("LastN")
	browser.find_element_by_name("email").send_keys("FirstN@LastN.com")

	current_dir = os.path.abspath(os.path.dirname("/home/linkin/Desktop/test"))
	file_path = os.path.join(current_dir, 'text.txt')
	browser.find_element_by_css_selector("input#file").send_keys(file_path)


	browser.find_element_by_css_selector("button.btn.btn-primary").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(8)
    # закрываем браузер после всех манипуляций
	browser.quit()

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
