from selenium import webdriver
import time
import math

# Считает формулу на странице
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

#Открывает браузер
try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    x_element = browser.find_element_by_id("input_value")   #находит переменную
    x = x_element.text                                      #присваивает ее за х
    y = calc(x)                                             #высчитывает формулу с х
    
    #находит поле для ввода ответа
    input1 = browser.find_element_by_xpath('//input[@type="text"]') 
    input1.send_keys(y)
    
    #найти и кликнуть по чекбоксу
    option1 = browser.find_element_by_xpath('//input[@type="checkbox"]')
    option1.click()

    #найти и кликнуть radiobutton
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
