from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name("input").send_keys("Ivan")
    browser.find_element_by_name('last_name').send_keys("Bal")
    browser.find_element_by_class_name('form-control.city').send_keys("Kyiv")
    browser.find_element_by_id('country').send_keys("Ukraine")
    button = browser.find_element_by_css_selector('button.btn').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

