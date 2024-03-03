from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin


# Функция для вычисления значения функции
def calc(x):
    return str(log(abs(12 * sin(int(x)))))


try:
    # Инициализация драйвера браузера
    browser = webdriver.Chrome()

    # Открытие страницы
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Явное ожидание, пока цена не станет $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажатие на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Получение значения x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычисление значения функции
    result = calc(x)

    # Ввод ответа в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # Нажатие на кнопку "Submit"
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Получение результата
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

finally:
    # Закрытие браузера
    browser.quit()
