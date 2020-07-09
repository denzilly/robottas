from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
import requests
from random import *
import sys
import time

sys.path.insert(1, '/modules')






driver = webdriver.Firefox(executable_path='modules/data/resources/geckodriver.exe')
driver.get("https://selenium-python.readthedocs.io/locating-elements.html")

time.sleep(2)

html = driver.find_element_by_tag_name("html")
# reduce zoom
html.send_keys(Keys.CONTROL, Keys.SUBTRACT)
html.send_keys(Keys.CONTROL, Keys.SUBTRACT)
html.send_keys(Keys.CONTROL, Keys.SUBTRACT)
html.send_keys(Keys.CONTROL, Keys.SUBTRACT)
html.send_keys(Keys.CONTROL, Keys.SUBTRACT)
# increment zoom
