from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def create_webdriver():
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(executable_path='modules/data/resources/geckodriver.exe', options = options)


    return driver