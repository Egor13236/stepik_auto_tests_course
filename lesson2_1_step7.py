from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = " http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #Смотрим формулу
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    #Находим x
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    #Выводим ответ в строку
    input = browser.find_element(By.ID, "answer")
    input.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    #Ставим галачку в чекбоксе
    option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    option1.click()
    #Выбираем нужный радиобатон
    #option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
