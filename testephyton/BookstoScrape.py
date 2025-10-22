from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Edge()

navegador.get("https://books.toscrape.com/")

time.sleep(5)

NomeLivro = navegador.find_element(By.TAG_NAME, "title")
print(NomeLivro)

time.sleep(20)

PrecoLivro = navegador.find_element(By.CLASS_NAME, "price_color")


time.sleep(20)