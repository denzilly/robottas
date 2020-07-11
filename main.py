
from modules.create_webdriver import create_webdriver
from modules.generator import get_name_email, get_dob, get_country
from modules.create_account import create_account
import time


import sys

# select up to 5 drivers
# select a team

start_time = time.time()
selected_drivers = ['A. Giovinazzi', 'V. Bottas']
team = "Alfa Romeo"


if __name__ == '__main__':


    webdriver = create_webdriver()
    webdriver.get("https://account.formula1.com/#/en/register?lead_source=web_fantasy&redirect=https%3A%2F%2Ffantasy.formula1.com%2Fteam%2Fcreate%3Ffrom%3Dsignup")

    #Creates an account with given drivers
    create_account(webdriver, selected_drivers, team)

    print("--- %s seconds ---" % (time.time() - start_time))

    time.sleep(5)
    webdriver.close()

