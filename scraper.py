from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import requests
import scrapy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

title_lists = []
testing_tile = []



PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)
# driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://go.boarddocs.com/vsba/fairfax/Board.nsf/Public"
url_to_district = dict()

driver.get("https://go.boarddocs.com/vsba/fairfax/Board.nsf/Public")
search = driver.find_element("id", "ui-id-3")
driver.execute_script("arguments[0].click();", search)
time.sleep(3)
a_tags = driver.find_elements(By.TAG_NAME, 'a')
for a_tag in a_tags:
    if a_tag.text != "" and "20" in a_tag.text:
        print(a_tag.text)
checked_a_tags = set()
while len(checked_a_tags) < len(a_tags):
    a_tags = driver.find_elements(By.TAG_NAME, 'a')
    for a_tag in a_tags:
        if a_tag.text not in checked_a_tags:
            testing_tile.append(a_tag.text)
            checked_a_tags.add(a_tag.text)
            if a_tag.text != "" and "20" in a_tag.text:
                print(a_tag.text)
                date = a_tag.text
                driver.execute_script("arguments[0].click();", a_tag)
                time.sleep(2)   
                try:
                    agenda = driver.find_element("id", "btn-view-agenda")
                except NoSuchElementException:
                    break
                driver.execute_script("arguments[0].click();", agenda)
                time.sleep(2)
                driver.find_element("xpath", "//button[@class='print']").click()
                time.sleep(2)
                driver.find_element("xpath", "//li[@class='print-agenda ui-tabs-tab ui-corner-top ui-state-default ui-tab']").click()
                time.sleep(2)
                agenda_details = driver.find_element("id", "tab-2")
                html_data = agenda_details.get_attribute("innerHTML")
                file_name = "Meetings/" + "vsba" + date + ".html"
                with open(file_name, 'w') as f:
                    f.write(html_data)
                f.close()
            # time.sleep(3)
                driver.get("https://go.boarddocs.com/vsba/fairfax/Board.nsf/Public")
                search = driver.find_element("id", "ui-id-3")
                driver.execute_script("arguments[0].click();", search)
                # time.sleep(4)
                # a_tags = driver.find_elements(By.TAG_NAME, 'a')
                # time.sleep(1)
                break

input("Press enter to exit")
