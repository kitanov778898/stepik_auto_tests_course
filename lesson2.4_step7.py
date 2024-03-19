from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
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
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    
    # 1) Открыть страницу 
    browser.get(link)

    first_window = browser.window_handles[0]
    print('first_window =',first_window)
    #button.click()
    
    # 2) Находим кнопку, которую надо нажать
    button = browser.find_element(By.ID, "book")

    # 3) говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    
    # 4) Нажать на кнопку
    button.click()
    #print('button.click()')
    
    # 5) Считать значение для переменной x.
    x_element = browser.find_element(By.ID, "input_value")
    valuex = x_element.text
    #print('x_element.text ', x_element.text)
    
    # 6) Посчитать математическую функцию от x (код для этого приведён ниже).
    z = calc(valuex)

    # 7) Ввести ответ в текстовое поле.
    input = browser.find_element(By.ID, "answer")
    input.send_keys(str(z))
    
    #8) Нажать кнопку "Submit"
    submit = browser.find_element(By.ID, "solve")

    browser.execute_script("window.scrollBy(0, 100);")

    WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID, "solve")))

    print('submit ', submit)
    submit.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(25)
    # закрываем браузер после всех манипуляций
    browser.quit()
    