from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

my_sum=0

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.ID, "num1")
    print(input1.text)

    #print('type')
    #print(type(int(input1.text)))
    
    input2 = browser.find_element(By.ID, "num2")
    print(input2.text)

    my_sum=int(input1.text)+int(input2.text)
    print('Sum = ', my_sum)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    print(select)
    select.select_by_visible_text(str(my_sum)) # ищем элемент с текстом my_sum
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()