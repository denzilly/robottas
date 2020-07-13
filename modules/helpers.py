import pandas as pd
import os
from bs4 import BeautifulSoup
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from pynput.mouse import Controller, Button
import time
import datetime



def click(x,y,count):
    mouse = Controller()
    mouse.position = (x,y)
    for x in range(count):
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.5)
        print("click")


## Update excel list of functional accounts
def update_accounts_list(new_account):

    path = os.path.dirname(os.path.abspath(__file__)) + "/data/logs/accounts.xlsx"
    df = pd.read_excel(path)


    df = df.append({'email': new_account[0], 'password': new_account[1]}, ignore_index=True)
    #remove duplicates
    df.drop_duplicates(subset = "email", keep = False, inplace = True)
    df.to_excel(path, index = False)


def save_prices(df,filename):

    path = os.path.dirname(os.path.abspath(__file__)) + f"/data/{filename}.xlsx"
    df = pd.read_excel(path)

    df = df.append({'email': new_account[0], 'password': new_account[1]}, ignore_index=True)
    # remove duplicates
    df.drop_duplicates(subset="email", keep=False, inplace=True)
    df.to_excel(path, index=False)


## Helper function to enter data into fields by xpath
def enter(driver, field, text):
       driver.find_element_by_xpath(field).send_keys(text)

def click_by_text(driver, tag, text):
    action = ActionChains(driver)
    xpath = f""".//{tag}[text()='{text}'] """

    action.move_to_element(driver.find_element_by_xpath(xpath))
    driver.find_element_by_xpath(xpath).click()

def zoom_out(driver, steps):
    driver.set_context("chrome")
    win = driver.find_element_by_tag_name("html")
    for x in range(steps-1):
        win.send_keys(Keys.CONTROL + "-")
    driver.set_context("content")
    print("zooming out")

def escape(driver):
    driver.set_context("chrome")
    win = driver.find_element_by_tag_name("h3")
    win.send_keys(Keys.ESCAPE)
    driver.set_context("content")
    print("zooming out")



## Wait for element to load
def element_load(driver, element, delay, type):

    if type == "class":
        try:
            element_present = EC.element_to_be_clickable((By.CLASS_NAME, element))
            WebDriverWait(driver, delay).until(element_present)
            print(f"detected {element}")
        except TimeoutException:
            print('class timed out')
    elif type == "xpath":
        try:
            element_present = EC.element_to_be_clickable((By.XPATH, element))
            WebDriverWait(driver, delay).until(element_present)
            print(f"detected {element}")
        except TimeoutException:
            print('xpath timed out')
    elif type == "css":
        try:
            element_present = EC.element_to_be_clickable((By.CSS_SELECTOR, element))
            WebDriverWait(driver, delay).until(element_present)
            print(f"detected {element}")
        except TimeoutException:
            print('css selector timed out')





## Parse innerHTML to get driver stats from list
def get_drivers(html):

    driver_df = pd.DataFrame()

    tags = {          "name" : "players-list__row__name",
                      "team" :"text--uppercase players-list__row__content__meta__item players-list__row__content__meta__item--team",
                      "picked" : "players-list__row__content__meta__item players-list__row__content__meta__item--picked",
                      "score" : "players-list__row__content__meta__item players-list__row__content__meta__item--score",
                      "price" :"players-list__row__price",

             }


    soup = BeautifulSoup(html, 'html.parser')
    driver_info_list = soup.findAll("li", {"class":"players-list__row"})

    #create a dataframe from each line of driver information in the table
    for x in driver_info_list:



        driver = { "name" : x.findChildren("span",{"class":tags["name"]})[0].text.strip(),
                   "team": x.findChildren("li", {"class": tags["team"]})[0].text.strip(),
                   "picked": x.findChildren("li", {"class": tags["picked"]})[0].text.strip(),
                   "score": x.findChildren("li", {"class": tags["score"]})[0].text.strip(),
                   "price": x.findChildren("div", {"class": tags["price"]})[0].text.strip(),

                }

        driver_df = driver_df.append(driver, ignore_index=True)

    return driver_df

# Select additional random drivers, but stay under budget
def update_driver_prices(df,filename):
    now = datetime.datetime.now()

    dprices_df = pd.read_excel(filename)


    #Create new row to add
    new_prices = {}
    new_prices['Timestamp'] = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)

    for row in df.iterrows():
        new_prices[row[1]['name']] = row[1]['price'][1:row[1]['price'].find("m")]
    new_row = pd.DataFrame.from_records([new_prices])

    print(new_row)

    #row[0] is driver name, 1 is pick rate,2 is price



    dprices_df = dprices_df.append(new_prices, ignore_index=True)
    dprices_df.to_excel('driver_prices.xlsx', index=False)










