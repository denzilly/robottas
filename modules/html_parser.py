from bs4 import BeautifulSoup
import pandas as pd



def get_drivers():

    with open('source.html') as f:
        html = f.read()

        driver_df = pd.DataFrame()

        tags = {          "name" : "players-list__row__name",
                          "team" :"text--uppercase players-list__row__content__meta__item players-list__row__content__meta__item--team",
                          "picked" : "players-list__row__content__meta__item players-list__row__content__meta__item--picked",
                          "score" : "players-list__row__content__meta__item players-list__row__content__meta__item--score",
                          "price" :"players-list__row__price",
                          "xpath_id" : "players-list__row__add-button"
                 }


        soup = BeautifulSoup(html, 'html.parser')

        driver_info_list = soup.findAll("li", {"class":"players-list__row"})
        for x in driver_info_list:
            driver = { "name" : x.findChildren("span",{"class":tags["name"]})[0].text.strip(),
                       "team": x.findChildren("li", {"class": tags["team"]})[0].text.strip(),
                       "picked": x.findChildren("li", {"class": tags["picked"]})[0].text.strip(),
                       "score": x.findChildren("li", {"class": tags["score"]})[0].text.strip(),
                       "price": x.findChildren("div", {"class": tags["price"]})[0].text.strip(),
                       "xpath_id": x.findChildren("button", {"class": tags["xpath_id"]})[0].get('id')
                    }
            driver_df = driver_df.append(driver, ignore_index= True)
        print(driver_df.loc[driver_df["name"] == "C. Leclerc"]["xpath_id"].item())





get_drivers()