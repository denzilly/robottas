from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from random import *
import sys
import time







sys.path.insert(1, '/modules')

from generator import get_name_email, get_dob, get_country
from xpaths import get_xpaths
from helpers import update_accounts_list, get_drivers

drivers = ['N. Latifi', 'G. Russell', 'K. Magnussen', 'A. Giovinazzi', 'L. Stroll', 'S. Perez']

def create_account(drivers):

    driver = webdriver.Firefox(executable_path='data/resources/geckodriver')
    driver.get("https://account.formula1.com/#/en/register?lead_source=web_fantasy&redirect=https%3A%2F%2Ffantasy.formula1.com%2Fteam%2Fcreate%3Ffrom%3Dsignup")

    name_email = get_name_email()
    password = randint(11111111,99999999)
    dob = get_dob()

    xpaths = get_xpaths()



    # helper functions

    def enter(field, text):
        driver.find_element_by_xpath(field).send_keys(text)

    #wait for page to load before doing stuff on page. If pageload > 10 seconds, shut down
    def element_load(element, delay, type):

        if type == "class":
            try:
                myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, element)))
            except TimeoutException:
                print('timed out')
        elif type == "xpath":
            try:
                myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, element)))
            except TimeoutException:
                print('timed out')


    element_load(xpaths['title'])

    ### Enter account details

    Select(driver.find_element_by_xpath(xpaths['title'])).select_by_value('Mr')
    enter(xpaths['first_name'], name_email[0])
    enter(xpaths['last_name'], name_email[1])

    enter(xpaths['dob_field'],dob)

    Select(driver.find_element_by_xpath(xpaths['country_of_residence'])).select_by_value(str(get_country()[0]))
    enter(xpaths['email_address'], name_email[2])
    enter(xpaths['password_field'], password )
    enter(xpaths['confirm_password_field'], password)

    print("data entered")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element_by_class_name("registrationform-submit").click()


    print(f"Account was created, adding credentials {name_email[2]},{password} to master list.")
    update_accounts_list([name_email[2], password])


    element_load(xpaths['add_driver'], xpaths['add_driver_alt'])

    try:
        driver.find_element_by_xpath(xpaths['add_driver']).click()
        driver.find_element_by_xpath(xpaths['add_driver_alt']).click()
    except NoSuchElementException:
        print("fuck you")



    time.sleep(5)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("-").key_up(Keys.CONTROL).perform();
    element = driver.find_element_by_class_name("lineup-picker__card__body__listing")
    html = element.get_attribute('innerHTML')
    driver_df = get_drivers(html)
    time.sleep(1)
    print(driver_df)
    time.sleep(5)


    for x in drivers:
        print(x)
        xpath = driver_df.loc[driver_df["name"] == x]["xpath_id"].item()
        print(xpath)
        #driver.find_element_by_xpath(xpath).click()
        time.sleep(1)






    driver.close()



create_account(drivers)

