import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//input[contains(@name, 'firstname') and @required]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[contains(@name, 'lastname') and @required]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[contains(@name, 'email') and @required]")
    input3.send_keys("Petrov@gmail.com")

    element = browser.find_element(By.CSS_SELECTOR, "[type='file']") # Находим загрузчик
    current_dir = os.path.abspath(os.path.dirname(__file__)) # находим директорию выполняемого скрипта
    file_name = "file.txt" # имя используемого файла
    file_path = os.path.join(current_dir, file_name) # путь до файла
    element.send_keys(file_path) # отправляем файл

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
