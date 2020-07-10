import pandas as pd
import os
from bs4 import BeautifulSoup


def update_accounts_list(new_account):

    path = os.path.dirname(os.path.abspath(__file__)) + "/data/resources/accounts.xlsx"
    df = pd.read_excel(path)


    df = df.append({'email': new_account[0], 'password': new_account[1]}, ignore_index=True)
    #remove duplicates
    df.drop_duplicates(subset = "email", keep = False, inplace = True)
    df.to_excel(path, index = False)



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
    for x in driver_info_list:

        xpath = "// *[ @ id = \"" + x.findChildren("button", {"class": tags["xpath_id"]})[0].get('id') + " \" ]"

        driver = { "name" : x.findChildren("span",{"class":tags["name"]})[0].text.strip(),
                   "team": x.findChildren("li", {"class": tags["team"]})[0].text.strip(),
                   "picked": x.findChildren("li", {"class": tags["picked"]})[0].text.strip(),
                   "score": x.findChildren("li", {"class": tags["score"]})[0].text.strip(),
                   "price": x.findChildren("div", {"class": tags["price"]})[0].text.strip(),
                   "xpath_id":  xpath
                }

        driver_df = driver_df.append(driver, ignore_index=True)

    return driver_df

