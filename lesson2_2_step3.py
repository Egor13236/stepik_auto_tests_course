from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Находим a,b
    a = browser.find_element(By.ID, "num1").text
    b = browser.find_element(By.ID, "num2").text
    #Считаем c
    c = str((int(a)+int(b)))

#Находит выплывающий список
#Выбирает строчку из списка
    #browser.find_element_by_id("dropdown").send_keys(c) 
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(c)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
