# Настройте виртуальное окружение на своем компе. Ниже ссылка на видео о виртуальных окружениях. 
# Там есть куча деталей. Если будут возникать проблемы, что-то будет не получаться - пишите.
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.google.com/')
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('cat')
search_input.submit()
driver.quit()