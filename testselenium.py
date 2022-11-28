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

# pagelinks_xpath = "//*[@id=\"meeting-accordion\"]"  # Site specific
pagelinks_xpath = "//*[@class=\"ui-accordion-header ui-corner-top ui-accordion-header-collapsed ui-corner-all ui-state-default\"]"  # Site specific
pagelinks = driver.find_elements("xpath", pagelinks_xpath)
pagelinks = pagelinks[:int(len(pagelinks))]
# print(pagelinks)
for link in pagelinks:
    # print(link.text)
    driver.execute_script("arguments[0].click();", link)
    sublinks_xpath = "//*[@class=\"wrap-year ui-accordion-content ui-corner-bottom ui-helper-reset ui-widget-content ui-accordion-content-active\"]"  # Site specific could replace wiht class
    sublinks = driver.find_elements("xpath", sublinks_xpath) # finds a whole block
    sublinks = sublinks[:int(len(sublinks))]
    for sublink in sublinks:
        # print(sublink.text)
        time.sleep(0.2)
        f.write(sublink.text)
        f.write("BREAKPOINT")
        title_lists.append(sublink.text)
        # driver.execute_script("arguments[0].click();", sublink)
        # time.sleep(1)
    # rectangle_path = "//*[@tabindex=\"0\"]"  # Site specific could replace wiht class
    # time.sleep(1)
    # rectangle = driver.find_elements("xpath", rectangle_path) # finds a whole block
    # time.sleep(1)
    
    # driver.find_element("xpath", "//a/]").click()

    # for rec in rectangle:
    #     time.sleep(1)
    #     driver.execute_script("arguments[0].click();", rec)
#     time.sleep(1)
# time.sleep(3)
# testing = driver.find_elements(By.TAG_NAME, 'a')
# for test in testing:
#     testing_tile.append(test.text)
#     if test.text != "" and "20" in test.text:
#         driver.execute_script("arguments[0].click();", test)
#         time.sleep(0.5)   
#         agenda = driver.find_element("id", "btn-view-agenda")
#         driver.execute_script("arguments[0].click();", agenda)
#         time.sleep(0.5)
#         driver.find_element("xpath", "//button[@class='print']").click()
#         time.sleep(0.5)
#         driver.find_element("xpath", "//li[@class='print-agenda ui-tabs-tab ui-corner-top ui-state-default ui-tab']").click()
        
#         # print_btn = driver.find_element("button", "print")
#         # driver.execute_script("arguments[0].click();", agenda)
#         # agenda = "//*[@id=\"btn-view-agenda\"]"
        
# print(testing_tile)

# # print(title_lists)
# # for title in title_lists:
# #     print(title)

#     # if "school board" in title or "sensor" in title or "vap" in title:
#     #     print("keyword")
# # # ui-accordion-header ui-corner-top ui-accordion-header-collapsed ui-corner-all ui-state-default
# # elements = driver.find_elements(By.CLASS_NAME, "ui-accordion-header")
# # print(len(elements))
# # for element in elements:
# #     driver.execute_script("arguments[0].click();", element)

input("Press enter to exit")

# pagelinks_text = [l.text for l in pagelinks]
# print(len(pagelinks_text))
# print(pagelinks_text)
# search = driver.find_element("id", "ui-id-22")
# driver.execute_script("arguments[0].click()", search)

# temp = driver.find_elements(By.XPATH, '//button')
# accordions = driver.find_elements(By.XPATH, '\\a[@data-parent=#accordion1]')
# elements = driver.find_elements(By.XPATH, "//*[@id=\"ui-id-18\"]")
# driver.execute_script("arguments[0].click()", elements)

# print(elements)



# print(accordions)
# clicks into meeting tab (above)






# page = requests.get(url)
# soup = BeautifulSoup (page.text, "html.parser")
# print(soup)


# select = Select(driver.find_element_by_id('li-meetings'))
# print(select.options[index].text) # date

# scrapy.Request(
#             "https://www.boarddocs.com/fl/palmbeach/board.nsf/XML-ActiveMeetings",
#             dont_filter=True,
#         )

# driver.close() #c loses tab
# driver.quit() # closes browser