from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math, os    

# объявим функцию calc()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
print('current_dir -', current_dir) 
file_path = os.path.join(current_dir, 'test_load.txt')           # добавляем к этому пути имя файла 
print('file_path -', file_path) 
#element.send_keys(file_path)

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    
    # 1) Открыть страницу 
    browser.get(link)

    first_window = browser.window_handles[0]
    print('first_window =',first_window)
    
    # 2) Нажать на кнопку
    input1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    input1.click()
    
    # 3) Принять confirm
    #confirm = browser.switch_to.alert
    #confirm.accept()

    new_window = browser.window_handles[1]
    print('new_window =',new_window)

    browser.switch_to.window(new_window)  #переключились на нужную вкладку

    # 3.1) В новом окне получаем число для расщетов
    x_element = browser.find_element(By.ID, "input_value")
    valuex = x_element.text
    print('x_element.text ', x_element.text)
    
    # 3.2) Посчитать математическую функцию от x (код для этого приведён ниже).
    z = calc(valuex)

    # 3.3) Ввести ответ в текстовое поле.
    input = browser.find_element(By.ID, "answer")
    input.send_keys(str(z))
    
    #4) Нажать кнопку "Submit"
    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(25)
    # закрываем браузер после всех манипуляций
    browser.quit()
    