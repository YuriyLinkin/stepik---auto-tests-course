import math 
import time 
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")

    browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000))).click()


    browser.find_element_by_tag_name("input").send_keys("Ivan")
    browser.find_element_by_name('last_name').send_keys("Bal")
    browser.find_element_by_class_name('form-control.city').send_keys("Kyiv")
    browser.find_element_by_id('country').send_keys("Ukraine")
    button = browser.find_element_by_css_selector('button.btn').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

