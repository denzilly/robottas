from bs4 import BeautifulSoup
import pandas as pd



def get_drivers(html):

    driver_df = pd.DataFrame()

    tags = {          "name" : "players-list__row__name",
                      "team" :"text--uppercase players-list__row__content__meta__item players-list__row__content__meta__item--team",
                      "picked" : "players-list__row__content__meta__item players-list__row__content__meta__item--picked",
                      "score" : "players-list__row__content__meta__item players-list__row__content__meta__item--score",
                      "price" :"players-list__row__price"
             }


    soup = BeautifulSoup(html, 'html.parser')

    driver_info_list = soup.findAll("li", {"class":"players-list__row"})
    for x in driver_info_list:
        driver = { "name" : x.findChildren("span",{"class":tags["name"]})[0].text.strip(),
                   "team": x.findChildren("li", {"class": tags["team"]})[0].text.strip(),
                   "picked": x.findChildren("li", {"class": tags["picked"]})[0].text.strip(),
                   "score": x.findChildren("li", {"class": tags["score"]})[0].text.strip(),
                   "price": x.findChildren("div", {"class": tags["price"]})[0].text.strip()
                }

        print(driver)
