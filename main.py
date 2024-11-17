import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = 'https://lambdatest.com/selenium-playground/jquery-dropdown-search-demo'

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# найти дроп и нажать (Select Multiple Values with search)
driver_chrome.find_element(
    By.XPATH, "//span[@class='select2-selection select2-selection--multiple']"
).click()
print("Нажатие на дроп.")

# пауза
time.sleep(2)

# найти и выбрать Аляску
driver_chrome.find_element(
    By.XPATH, "(//li[@class='select2-results__option'])[1]"
).click()
print("Выбор из списка Аляски.")
