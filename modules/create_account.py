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

from generator import get_name_email, get_dob, get_country
from xpaths import get_xpaths
from helpers import update_accounts_list, get_drivers



def create_account():

    driver = webdriver.Firefox(executable_path='data/resources/geckodriver.exe')
    driver.get("https://account.formula1.com/#/en/register?lead_source=web_fantasy&redirect=https%3A%2F%2Ffantasy.formula1.com%2Fteam%2Fcreate%3Ffrom%3Dsignup")

    name_email = get_name_email()
    password = randint(11111111,99999999)
    dob = get_dob()

    xpaths = get_xpaths()



    # helper functions

    def enter(field, text):
        driver.find_element_by_xpath(field).send_keys(text)

    #wait for page to load before doing stuff on page. If pageload > 10 seconds, shut down
    def element_load(element, *backupelement):
        counter = 0
        while True:
            try:
                if counter % 2 == 0:
                    print(driver.find_element_by_xpath(element).text)

                else:
                    print(driver.find_element_by_xpath(element).text)
                time.sleep(2)
                break
            except:
                if counter >= 50:
                    print("Unknown pageload error")
                    driver.close()
                    sys.exit()
                print("page not loaded yet")
                time.sleep(0.1)
                counter += 0.1




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
    driver.find_element_by_xpath(xpaths['register_btn']).click()


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
    get_drivers(html)
    time.sleep(5)




    #driver.close()



create_account()

