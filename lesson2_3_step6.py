from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
# Узнаем имя новой вкладки
    new_window = browser.window_handles[1]  
# Запоминаем имя 1 вкладки
#first_window = browser.window_handles[0]  
# Переходим на новую вкладку
    browser.switch_to.window(new_window)
          
    #Смотрим формулу
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    #Находим x
    x = browser.find_element(By.ID, "input_value").text
    #Считаем y
    y = calc(x)
    #Выводим ответ в строку
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # Нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
