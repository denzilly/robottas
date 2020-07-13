from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import platform
import os

def create_webdriver():
    options = Options()
    #options.headless = True

    path = os.path.dirname(os.path.abspath(__file__)) + "/data/resources/"

    #select correct geckodriver for your system
    if "Windows" in platform.system():
        print("Windows OS")
        driver = webdriver.Firefox(executable_path= path+ 'geckodriver.exe', options = options)
    elif "Linux" in platform.system():
        print("Linux OS")
        print(path)
        driver = webdriver.Firefox(executable_path= path + 'geckodriver', options = options)

    return driver

