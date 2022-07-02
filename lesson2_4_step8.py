from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
btn = browser.find_element_by_id('book')
btn.click()
button = browser.find_element(By.TAG_NAME, "button") # листаем страницу что-бы было видно Submit и robotsRule
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value') # ищем по id чему равен X
x = x_element.text # берём значение
y = calc(x) # считаем по формуле
element1 = browser.find_element(By.ID, 'answer') # находим поле куда нужно отправить ответ из формулы
element1.send_keys(y)
    # Отправляем заполненную форму
button = browser.find_element(By.ID, 'solve')
button.click()