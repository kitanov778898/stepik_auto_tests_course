from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math    
# Импорт модуля math 

# объявим функцию my_function()
def calc(x):
    x = math.log(abs(12*math.sin(int(x))))
    return x 
    print(x)

try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()

    # 1) Открыть страницу https://suninjuly.github.io/math.html.
    browser.get(link)


    # 2) Считать значение для переменной x.
    x_element = browser.find_element(By.ID, "input_value")
    #print(x_element.text)

    x = x_element.text

    # 3) Посчитать математическую функцию от x (код для этого приведён ниже).
    z = calc(x)

    #z=math.log(math.fabs(12*math.sin(x)))
    #print('sin(x) = ', math.sin(x))
    #print('12*sin(x) = ', 12*math.sin(x) )
    #print('abs(12*sin(x)) = ', abs(12*math.sin(x)))
    #print('log(abs(12*sin(x))) = ', math.log(abs(12*math.sin(x))))
    print('z =', z)

    # проскроллит страницу на 100 пикселей вниз
    #browser.execute_script("window.scrollBy(0, 100);")

    # элемент после скролла оказался в области видимости.
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # 4) Ввести ответ в текстовое поле.
    input3 = browser.find_element(By.ID, "answer")
    input3.send_keys(str(z))

    # 5) Отметить checkbox "I'm the robot".
    input2 = browser.find_element(By.CLASS_NAME, "form-check-label")
    print(input2)
    input2.click()
    #print('click')

    # 6) Выбрать radiobutton "Robots rule!".


    #input3 = browser.find_element(By.ID, "answer")
    #input3.send_keys(str(z))
    

    # Отправляем заполненную форму
    button2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    browser.execute_script("window.scrollBy(0, 100);")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(300)
    # закрываем браузер после всех манипуляций
    browser.quit()