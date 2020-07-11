from bs4 import BeautifulSoup
import pandas as pd



def get_drivers():

    with open('source.html') as f:
        html = f.read()

        driver_df = pd.DataFrame()

        soup = BeautifulSoup(html, 'html.parser')

        all = soup.findAll("option")
        for x in all:
            print(x['value'])






get_drivers()