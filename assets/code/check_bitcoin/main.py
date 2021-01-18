#!/usr/bin/env python3

################################################################
# Example of using AlphaVantage API
# Sign up to get an API key and import it
# This script currently just gets the 5 latest values for bitcoin but can do others as well
# will eventually replace my powershell script at https://automationadmin.com/2020/09/ps-send-email-bitcoin
################################################################

import requests
from dotenv import load_dotenv
import os
import json
import math
from time import sleep
import logging
import logging.handlers
from datetime import datetime
import helpers

helpers.load_logging()
load_dotenv()
logging.info("Starting...")

logging.info("Loading environment vars...")
try:
    api_key = os.environ["API_KEY"]
    email_user = os.environ["GMAIL_USER"]
    email_password = os.environ["GMAIL_PASSWORD"]
    email_to = os.environ["MAIL_RECEIVER"]
except KeyError:
    logging.error("Unable to get environmental variables")
except Exception as e:
    logging.error("Generic catch: Unable to get environmental variables")
    logging.error("Generic catch: " + str(e))
logging.info("Loading environment vars...completed")

def main():

    logging.info("Sending API Request...")

    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey={api_key}"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
    }
    r = requests.request("GET", url, headers=headers, data=payload)
    req = r.json()
    logging.info("Sending API Request...completed")

    ## sort the responses
    keylist = list(req['Time Series (Digital Currency Daily)'].keys())
    keylist.sort(reverse=True)

    ## give me just the top 5
    first_five_list = keylist[0:5]
    
    # now that we see the top five, store in variables for comparisons
    first_key = first_five_list[0]
    first_value = req['Time Series (Digital Currency Daily)'][first_key]['4b. close (USD)']
    first_value = math.floor(float(first_value))

    second_key = first_five_list[1]
    second_value = req['Time Series (Digital Currency Daily)'][second_key]['4b. close (USD)']
    second_value = math.floor(float(second_value))


    third_key = first_five_list[2]
    third_value = req['Time Series (Digital Currency Daily)'][third_key]['4b. close (USD)']
    third_value = math.floor(float(third_value))

    fourth_key = first_five_list[3]
    fourth_value = req['Time Series (Digital Currency Daily)'][fourth_key]['4b. close (USD)']
    fourth_value = math.floor(float(fourth_value))

    fifth_key = first_five_list[4]
    fifth_value = req['Time Series (Digital Currency Daily)'][fifth_key]['4b. close (USD)']
    fifth_value = math.floor(float(fifth_value))

    logging.info("Values for the last five days:")
    logging.info(f"{first_key}: {first_value}")
    logging.info(f"{second_key}: {second_value}")
    logging.info(f"{third_key}: {third_value}")
    logging.info(f"{fourth_key}: {fourth_value}")
    logging.info(f"{fifth_key}: {fifth_value}")

    # I will actually just grab the first 3 days
    if first_value < second_value < third_value :
        logging.info("Trend is downwards for three days straight")
        # Here I will send an email to buy if down for 3 days straight
        logging.info("Sending email...")
        send = helpers.send_email(email_user, email_password, email_to)
        logging.info(f"Sending email status: {send}")
    else:
        logging.info("Trend is not downwards for three days straight")
    
    logging.info("Completed")

if __name__ == '__main__':
    main()
else:
    pass