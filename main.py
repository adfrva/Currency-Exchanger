import requests
from datetime import datetime

def get_string_date():
    date = datetime.now()

    year = date.strftime("%Y")
    month = date.strftime("%m")
    day = date.strftime("%d")
    todays_date = f"{year}-{month}-{day}"
    
    return todays_date

print("Welcome to the Python Currency Exchange!")

today = get_string_date()
base_url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/"

print(today)
# Format for API calls
# https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@/latest/{date}/{endpoint}

from_currency = input("Which currency are you exchanging?: ")
to_currency = input("Which currency would you like?: ")
initial_amount = input("Enter how much you'd like to exchange: ")