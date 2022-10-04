import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


#Открыть страницу
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome() 
browser.get(link)


#Нажать на кнопку
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

#Принять confirm
confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
x = x_element.text
y = calc(x)

value = browser.find_element(By.ID, "answer")
value.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()



# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(10)







