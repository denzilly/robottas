
from modules.create_webdriver import create_webdriver
from modules.generator import get_name_email, get_dob, get_country
from modules.get_prices import get_prices
import time


import sys

# select up to 5 drivers
# select a team

start_time = time.time()
selected_drivers = ['A. Giovinazzi', 'V. Bottas']
team = "Alfa Romeo"


if __name__ == '__main__':

    for x in range(10):

        webdriver = create_webdriver()
        webdriver.get("https://fantasy.formula1.com/team/1?week=3")

        credentials = {
            'username' : 'bstevensonssss@gmail.com',
            'password' : 'ferrari'
        }

        #Creates an account with given drivers
        try:
            get_prices(webdriver, credentials)
        except:
            print ("Unexpected error:", sys.exc_info()[0])
            raise
        print("--- %s seconds ---" % (time.time() - start_time))

        time.sleep(5)
        webdriver.close()

