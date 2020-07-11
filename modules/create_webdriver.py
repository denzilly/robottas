from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import platform

def create_webdriver():
    options = Options()
    options.headless = True


    #select correct geckodriver for your system
    if "Windows" in platform.system():
        driver = webdriver.Firefox(executable_path='modules/data/resources/geckodriver.exe', options = options)
    elif "Linux" in platform.system():
        driver = webdriver.Firefox(executable_path='modules/data/resources/geckodriver', options=options)


    return driver