
from modules.xpaths import get_xpaths
from modules.helpers import *



import time



def get_prices(webdriver, credentials):


    webdriver.set_window_size(1920, 1080)
    xpaths = get_xpaths()
    ## Load account page

    ### Enter account details

    element_load(webdriver, xpaths['sign_in_btn'], 10, "css")
    webdriver.find_element_by_class_name(xpaths['username']).send_keys(credentials['username'])
    webdriver.find_element_by_class_name(xpaths['password']).send_keys(credentials['password'])
    webdriver.find_element_by_css_selector(xpaths['sign_in_btn']).click()


    element_load(webdriver, xpaths["swap_driver_1"], 10, "class")
    time.sleep(5)
    webdriver.find_element_by_class_name(xpaths['swap_driver_1']).click()


    element_load(webdriver, xpaths["next_1"], 10, "xpath")
    click_by_text(webdriver, 'div', 'Next')
    element_load(webdriver, xpaths["next_1"], 10, "xpath")
    click_by_text(webdriver, 'div', 'Next')
    element_load(webdriver, xpaths["done"], 10, "xpath")
    webdriver.find_element_by_xpath(xpaths['done']).click()

    time.sleep(2)
    element_load(webdriver, xpaths["expose_list"], 10, "xpath")
    webdriver.find_element_by_xpath(xpaths['expose_list']).click()
    #click_by_text(webdriver, 'div', 'Done')



    # Zoom out the page
    zoom_out(webdriver, 5)

    click_by_text(webdriver, 'span', 'DR')

    element = webdriver.find_element_by_class_name(xpaths['driver_card'])
    html = element.get_attribute('innerHTML')
    driver_df = get_drivers(html)
    driver_df.to_excel("driver_df.xlsx", index = False)
    print(driver_df)

    update_driver_prices(pd.read_excel('driver_df.xlsx'), 'driver_prices.xlsx')


    click_by_text(webdriver, 'span', 'CR')
    element = webdriver.find_element_by_class_name(xpaths['driver_card'])
    html = element.get_attribute('innerHTML')
    constructor_df = get_drivers(html)
    constructor_df.to_excel("constructor_df.xlsx", index=False)
    print(constructor_df)

    update_driver_prices(pd.read_excel('constructor_df.xlsx'), 'constructor_prices.xlsx')



