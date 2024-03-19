from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math    
# Импорт модуля math 

# объявим функцию my_function()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()

    # 1) Открыть страницу 
    browser.get(link)

    # 2.0
    # 2) Считать значение для переменной x.
    x_element = browser.find_element(By.ID, "input_value")
    #x_element = browser.find_element(By.cssSelector, "img")
    #valuex = x_element.get_attribute("valuex")
    valuex = x_element.text
    print('x_element.text ', x_element.text)
    
    # 3) Посчитать математическую функцию от x (код для этого приведён ниже).
    z = calc(valuex)

    browser.execute_script("window.scrollBy(0, 100);")

    # элемент после скролла оказался в области видимости.
    #button = browser.find_element(By.TAG_NAME, "button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # 4) Ввести ответ в текстовое поле.
    input = browser.find_element(By.ID, "answer")
    input.send_keys(str(z))

    # 5) Отметить checkbox "I'm the robot".
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    time.sleep(2)
   
    # 6) Выбрать radiobutton "Robots rule!".
    radiobutton = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    #print(radiobutton)
    radiobutton.click()
    
    # Отправляем заполненную форму
    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(25)
    # закрываем браузер после всех манипуляций
    browser.quit()