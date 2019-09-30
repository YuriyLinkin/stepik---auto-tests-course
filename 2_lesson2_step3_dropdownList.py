#import math
import time
from selenium import webdriver

def add(x,y):
	return int(x) + int(y)

try:
 
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/selects1.html") #/selects2.html

	x = browser.find_element_by_xpath("//*[@id='num1']").text
	y = browser.find_element_by_xpath("//*[@id='num2']").text
	summ = add(x,y)

	browser.find_element_by_tag_name("select").click()
	browser.find_element_by_css_selector("option[value='"+str(summ)+"']").click()
	browser.find_element_by_xpath("//*[@type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(15)
    # закрываем браузер после всех манипуляций
	browser.quit()
