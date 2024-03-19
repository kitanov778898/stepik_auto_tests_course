from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math, os    

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
print('current_dir -', current_dir) 
file_path = os.path.join(current_dir, 'test_load.txt')           # добавляем к этому пути имя файла 
print('file_path -', file_path) 
#element.send_keys(file_path)

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    
    # 1) Открыть страницу 
    browser.get(link)
    
    # 2) Заполнить текстовые поля: имя, фамилия, email
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('test')
    
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('test')
    
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys('test')
    
    # 3) Загрузить файл. Файл
    input4 = browser.find_element(By.ID, "file")
    print('input4 - ',input4)
    input4.send_keys(file_path)
    
    #4) Нажать кнопку "Submit"
    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(25)
    # закрываем браузер после всех манипуляций
    browser.quit()
    