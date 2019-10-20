import pytest
import math
import time
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_open_every_newlink(browser, number):
    browser.get(f"https://stepik.org/lesson/{number}/step/1")

    print("\nfinding TextAreaElement and typing Answer...")
    time.sleep(6)
    answer = str(math.log(int(time.time())))
    time.sleep(3)
    browser.find_element_by_xpath("//*[@placeholder='Type your answer here...']").send_keys(answer)
    time.sleep(3)
    browser.find_element_by_css_selector("button.submit-submission").click()

    time.sleep(3)
    print("\nmatching pop-upMessage 'Correct!'...")
    assert "Correct!" == browser.find_element_by_css_selector("pre.smart-hints__hint").text


