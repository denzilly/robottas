from random import *
import csv

from bs4 import BeautifulSoup
import requests

#### This script generates personal information
#name
#phone number
#email address
#address


################### GET PHONE NUMBER ####################################

def get_phone():
    phone_no = "064" + str(randint(1000000,9999999))

    return phone_no

#################### GET NAME AND EMAIL ADDRESS ############################


def csv_scrape(index, filename):
    with open(filename, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = [row[0] for idx, row in enumerate(csv_reader) if idx in(index, index)]

        return rows


def get_name_email():


    #Select first and last name at random from a list
    firstnum = randint(1,9500)
    lastnum = randint(1,9500)
    


    #seperate call statements because we need these for the emails
    first_name = csv_scrape(firstnum,'data/resources/voornamen.csv')[0]
    last_name = csv_scrape(lastnum,'data/resources/achternamen.csv')[0]

    full_name = first_name + " " + last_name
    print (full_name)

    r1 = randint(1,3)
    r2 = randint(1,3)
    r3 = randint(1,2)
    r4 = randint(0,5)

    #abbreviate name in email?
    if (r1 == 1):
        fname = first_name[0]
        lname = last_name
    elif (r1 == 2):
        fname = first_name[:len(first_name)-1]
        lname = last_name[0]
    else:
        fname = first_name[:len(first_name)-1]
        lname = last_name

    #period or underscore separator?
    if (r2 == 1):
        sep = ""
    elif(r2 == 2):
        sep = "."
    else:
        sep = "_"

    #Number at the end?
    if (r3 == 1):
        num = randint(23,99)
    else:
        num = ""

    # Select a Domain
    domains = ["@gmail.com", "@yahoo.com", "@xs4all.nl", "@kpnmail.nl", "@hotmail.com", "@live.com"]
    domain = domains[r4]

    #Piece it all together
    email = fname + sep + lname + str(num) + domain

    print(email)
    return first_name, last_name, email


#### DOB


def append_zero(digit):
    if len(digit) < 2:
        return "0" + digit

    else:
        return digit

def get_dob():

    day = append_zero(str(randint(1,28)))
    month = append_zero(str(randint(1,12)))
    year = str(randint(1950,1995))


    return  month + day + year



def get_country():

   return csv_scrape(randint(1,249), 'data/resources/ISO_countries.csv')


