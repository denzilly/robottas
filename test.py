import datetime
import pandas as pd
now = datetime.datetime.now()


def update_driver_prices(df):

    dprices_df = pd.read_excel('driver_prices.xlsx')


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


    columns = ['N. Latifi', 'G. Russell', 'K. Magnussen',
                       'A. Giovinazzi', 'L. Stroll', "L. Hamilton",
                       "V. Bottas", "M. Verstappen", "C. Leclerc",
                       "S. Vettel", "A. Albon", "C. Sainz",
                       "D. Ricciardo", "L. Norris", "E. Ocon",
                       "P. Gasly", "K. Raikkonen", "D. Kvyat",
                       "S. Perez", "R. Grosjean"]


update_driver_prices(pd.read_excel('driver_df.xlsx'))
