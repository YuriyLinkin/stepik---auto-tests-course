from selenium import webdriver
import time

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_css_selector('div.first_block .form-control.first').send_keys("FN-Success!")
    browser.find_element_by_css_selector('div.first_block .form-control.second').send_keys("LN-Success!")
    browser.find_element_by_css_selector('div.first_block .form-control.third').send_keys("Success@email.com")

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст и записываем
    welcome_text = browser.find_element_by_tag_name("h1").text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
