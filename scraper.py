from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import requests
import scrapy

title_lists = []
testing_tile = []

with open('testselenium.txt', 'w') as f:
    f.write('School Board Meeting Titles')
f = open("testselenium.txt", "a")

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)
# driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://go.boarddocs.com/vsba/fairfax/Board.nsf/Public"
driver.get("https://go.boarddocs.com/vsba/fairfax/Board.nsf/Public")
search = driver.find_element("id", "ui-id-3")
driver.execute_script("arguments[0].click();", search)
time.sleep(3)
testing = driver.find_elements(By.TAG_NAME, 'a')
for test in testing:
    testing_tile.append(test.text)
    if test.text != "" and "20" in test.text:
        driver.execute_script("arguments[0].click();", test)
        time.sleep(0.5)   
        agenda = driver.find_element("id", "btn-view-agenda")
        driver.execute_script("arguments[0].click();", agenda)
        time.sleep(0.5)
        driver.find_element("xpath", "//button[@class='print']").click()
        time.sleep(0.5)
        driver.find_element("xpath", "//li[@class='print-agenda ui-tabs-tab ui-corner-top ui-state-default ui-tab']").click()
        