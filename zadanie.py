from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    #link = "http://suninjuly.github.io/registration1.html" # Тест успешно проходит
    link = "http://suninjuly.github.io/registration2.html" # Тест падает с ошибкой
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    #--- First name ---
    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    #print(input1)
    input1.send_keys("Ivan")

    #--- Last name ---
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    #print(input1)
    input2.send_keys("Kitanov")

    #--- Email ---
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    #print(input1)
    input3.send_keys("Kitanov@test.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()