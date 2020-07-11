from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from modules.generator import get_name_email, get_dob, get_country
from modules.xpaths import get_xpaths
from modules.helpers import *

from random import *
import sys

import time


def create_account(webdriver, selected_drivers, team):
    ## Generate Account Details ##
    name_email = get_name_email()
    password = randint(11111111, 99999999)
    dob = get_dob()
    xpaths = get_xpaths()

    webdriver.set_window_size(1920, 1080)

    ## Load account page
    time.sleep(1)
    element_load(webdriver, xpaths['title'], 10, "xpath")



    ### Enter account details

    Select(webdriver.find_element_by_xpath(xpaths['title'])).select_by_value('Mr')
    enter(webdriver, xpaths['first_name'], name_email[0])
    enter(webdriver, xpaths['last_name'], name_email[1])

    enter(webdriver, xpaths['dob_field'], dob)

    Select(webdriver.find_element_by_id("Country-input")).select_by_value(str(get_country()[0]))
    enter(webdriver, xpaths['email_address'], name_email[2])
    enter(webdriver, xpaths['password_field'], password)
    enter(webdriver, xpaths['confirm_password_field'], password)

    print("data entered")

    webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    webdriver.find_element_by_class_name("registrationform-submit").click()

    print(f"Account was created, adding credentials {name_email[2]},{password} to master list.")
    update_accounts_list([name_email[2], password])

    ### Click through to driver list
    element_load(webdriver, xpaths['add_driver_class'], 10, "class")

    webdriver.find_element_by_class_name(xpaths['add_driver_class']).click()

    element_load(webdriver, xpaths["driver_card"], 10, "class")
    # Zoom out the page
    zoom_out(webdriver, 5)

    element = webdriver.find_element_by_class_name(xpaths['driver_card'])
    html = element.get_attribute('innerHTML')
    driver_df = get_drivers(html)
    print(driver_df)

    drivers = create_team(driver_df, selected_drivers, team)

    for x in drivers:
        xpath = driver_df.loc[driver_df["name"] == x]["xpath_id"].item()
        webdriver.find_element_by_xpath(xpath).click()





    element_load(webdriver,xpaths['driver_card'], 10, "class")
    html = element.get_attribute('innerHTML')
    constructor_df = get_drivers(html)
    print(constructor_df)
    xpath = constructor_df.loc[constructor_df["name"] == team]["xpath_id"].item()
    webdriver.find_element_by_xpath(xpath).click()


    element_load(webdriver,xpaths['driver_next'],10, "class")
    webdriver.find_element_by_class_name( xpaths['driver_next']).click()


    #pick turbo driver (always first one)
    element_load(webdriver, xpaths['turbo_driver'], 10, "class")
    webdriver.find_element_by_class_name(xpaths['turbo_driver']).click()
    webdriver.find_element_by_class_name(xpaths['turbo_next']).click()

    #pick favorite team (always first one)
    element_load(webdriver, xpaths['fav_team'], 10, "class")
    webdriver.find_element_by_class_name(xpaths['fav_team']).click()
    webdriver.find_element_by_class_name(xpaths['fav_team_next']).click()

    print("Team Successfully Created")
