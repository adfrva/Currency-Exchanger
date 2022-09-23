import requests
print("Welcome to the Python Currency Exchange!")

url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@/latest/"
# Format for API calls
# https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@/latest/{date}/{endpoint}


api_response = requests.get("https://api.exchangeratesapi.io/v1/")

from_currency = input("Which currency are you exchanging?: ")
to_currency = input("Which currency would you like?: ")
initial_amount = input("Enter how much you'd like to exchange: ")