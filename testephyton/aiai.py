from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Edge()

navegador.get("https://duckduckgo.com/")

time.sleep(5)

campo = navegador.find_element(By.NAME, "q")

campo.send_keys("Sorvete")
campo.send_keys(Keys.ENTER)

time.sleep(5)

