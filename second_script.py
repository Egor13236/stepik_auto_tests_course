from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "submit_button")
button.click()

# если нужно зактыть только одну открывшуюся вкладку используем browser.close()
# закрываем браузер после всех манипуляций
browser.quit()