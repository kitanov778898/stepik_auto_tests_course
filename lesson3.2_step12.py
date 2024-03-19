from selenium import webdriver
from selenium.webdriver.common.by import By
import time, unittest 

class TestSeal(unittest.TestCase):
    #def setUp(self):
     #   link = "http://suninjuly.github.io/registration1.html"
      #  browser = webdriver.Chrome()
       # browser.get(link)
        
    def test_my1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        #--- First name ---
        input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        #print(f"input1 - {input1.text}")
        #--- Last name ---
        input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input2.send_keys("Kitanov")
        #--- Email ---
        input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
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
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text, "ожидаемый текст совпадает с текстом на странице сайта")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
        #self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_my2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        #--- First name ---
        input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        #print(f"input1 - {input1.text}")
        #--- Last name ---
        input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input2.send_keys("Kitanov")
        #--- Email ---
        input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
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
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text, "ожидаемый текст совпадает с текстом на странице сайта")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
        #self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

        
if __name__ == "__main__":
    unittest.main()