import requests
import json
from datetime import datetime

# Prompt user to choose cryptocurrency symbol and target currency
crypto_symbol = input("Enter the cryptocurrency symbol (e.g., BTC for Bitcoin): ").upper()
currency_symbol = input("Enter the target currency symbol (e.g., USD for US Dollar): ").upper()

# Define the API endpoint and parameters
url = 'https://min-api.cryptocompare.com/data/v2/histohour'
params = {'fsym': crypto_symbol, 'tsym': currency_symbol, 'limit': '10', 'aggregate': '1'}

# Add your API key in the headers
headers = {'authorization': 'Your-API-Key'}

# Make the API request
response = requests.post(url, params=params, headers=headers)

# Check if the response is successful
if response.status_code == 200:
    # Parse JSON data
    data = response.json()
    print(f"\nHistorical {crypto_symbol} Price Data in {currency_symbol} (last 10 hours):\n")

    # Access the 'Data' field where historical data is stored
    if "Data" in data and "Data" in data["Data"]:
        for record in data["Data"]["Data"]:
            # Convert the timestamp to a readable date-time format
            time = datetime.fromtimestamp(record['time']).strftime('%Y-%m-%d %H:%M:%S')
            high = record['high']
            low = record['low']
            open_price = record['open']
            close_price = record['close']
            volume = record['volumefrom']

            # Print each record in a formatted way
            print(f"Time: {time}")
            print(f"  Open Price: {open_price} {currency_symbol}")
            print(f"  High Price: {high} {currency_symbol}")
            print(f"  Low Price: {low} {currency_symbol}")
            print(f"  Close Price: {close_price} {currency_symbol}")
            print(f"  Volume: {volume}\n")
    else:
        print("No historical data found.")
else:
    print("Error: could not retrieve data.")
