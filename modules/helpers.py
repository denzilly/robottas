import pandas as pd
import os
from bs4 import BeautifulSoup
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from random import *



## Update excel list of functional accounts
def update_accounts_list(new_account):

    path = os.path.dirname(os.path.abspath(__file__)) + "/data/logs/accounts.xlsx"
    df = pd.read_excel(path)


    df = df.append({'email': new_account[0], 'password': new_account[1]}, ignore_index=True)
    #remove duplicates
    df.drop_duplicates(subset = "email", keep = False, inplace = True)
    df.to_excel(path, index = False)


## Helper function to enter data into fields by xpath
def enter(driver, field, text):
       driver.find_element_by_xpath(field).send_keys(text)



def zoom_out(driver, steps):
    driver.set_context("chrome")
    win = driver.find_element_by_tag_name("html")
    for x in range(steps-1):
        win.send_keys(Keys.CONTROL + "-")
    driver.set_context("content")
    print("zooming out")



## Wait for element to load
def element_load(driver, element, delay, type):

    if type == "class":
        try:
            element_present = EC.element_to_be_clickable((By.CLASS_NAME, element))
            WebDriverWait(driver, delay).until(element_present)
            #print(f"detected {element}")
        except TimeoutException:
            print('class timed out')
    elif type == "xpath":
        try:
            element_present = EC.element_to_be_clickable((By.XPATH, element))
            WebDriverWait(driver, delay).until(element_present)
           # print(f"detected {element}")
        except TimeoutException:
            print('xpath timed out')





## Parse innerHTML to get driver stats from list
def get_drivers(html):

    driver_df = pd.DataFrame()

    tags = {          "name" : "players-list__row__name",
                      "team" :"text--uppercase players-list__row__content__meta__item players-list__row__content__meta__item--team",
                      "picked" : "players-list__row__content__meta__item players-list__row__content__meta__item--picked",
                      "score" : "players-list__row__content__meta__item players-list__row__content__meta__item--score",
                      "price" :"players-list__row__price",
                      "xpath_id": "players-list__row__add-button"
             }


    soup = BeautifulSoup(html, 'html.parser')
    driver_info_list = soup.findAll("li", {"class":"players-list__row"})

    #create a dataframe from each line of driver information in the table
    for x in driver_info_list:

        xpath = "//*[@id =\"" + x.findChildren("button", {"class": tags["xpath_id"]})[0].get('id') + "\" ]"

        driver = { "name" : x.findChildren("span",{"class":tags["name"]})[0].text.strip(),
                   "team": x.findChildren("li", {"class": tags["team"]})[0].text.strip(),
                   "picked": x.findChildren("li", {"class": tags["picked"]})[0].text.strip(),
                   "score": x.findChildren("li", {"class": tags["score"]})[0].text.strip(),
                   "price": x.findChildren("div", {"class": tags["price"]})[0].text.strip(),
                   "xpath_id":  xpath
                }

        driver_df = driver_df.append(driver, ignore_index=True)

    return driver_df

# Select additional random drivers, but stay under budget
def create_team(driver_df, selected_drivers, team):




    all_drivers = ['N. Latifi', 'G. Russell', 'K. Magnussen',
                   'A. Giovinazzi', 'L. Stroll', "L. Hamilton",
                   "V. Bottas", "M. Verstappen", "C. Leclerc",
                   "S. Vettel", "A. Albon", "C. Sainz",
                   "D. Ricciardo", "L. Norris", "E. Ocon",
                   "P. Gasly", "K. Raikkonen", "D. Kvyat",
                   "S. Perez", "R. Grosjean"]

    #messy, but necessary for now
    team_prices = {
        'Mercedes' : 32.2,
        'Ferrari' : 26.8,
        'Red Bull' : 24.5,
        'Mclaren' : 15.7,
        'AlphaTauri' : 12.9,
        'Renault' : 12.3,
        'Racing Point' : 10.2,
        'Alfa Romeo' : 8.5,
        'Haas' : 7.6,
        'Williams' : 6.5,
    }

    orig_drivers = selected_drivers
    # team_price = constructor_df.loc[constructor_df["name"] == team]["price"].item()
    team_budget = 100 - team_prices[team]

    for x in orig_drivers:
        driver_price = driver_df.loc[driver_df["name"] == x]["price"].item()
        team_budget -= float(driver_price[1:len(driver_price) - 1])
        orig_budget = team_budget

    while len(selected_drivers) < 5:

        #pick new drivers but no duplicates
        new_driver = all_drivers[randint(0, len(all_drivers)-1)]
        if new_driver not in selected_drivers:
            selected_drivers.append(new_driver)
            driver_price = driver_df.loc[driver_df["name"] == new_driver]["price"].item()
            team_budget -= float(driver_price[1:len(driver_price) - 1])

        #if your team is too expensive, start over
        if team_budget < 0:
            selected_drivers = orig_drivers
            team_budget = orig_budget


    print(f"Your selected drivers are: {selected_drivers}")
    print(f"You spent {100 - team_budget}")


    return selected_drivers








