#initial variables and imports from example
rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]
import requests
import xmltodict
import json
import random

#create a user input to allow the selection of a currency
def selectCurrency():
    flag = 1
    print("currencies to choose from:")
    string = " "
    for i in ratesForBase:
        print(i)
    while flag == 1:
        sel = input("select a currency").upper()
        #print(sel.upper())
        if sel in ratesForBase:
            print(f"{sel} is selected")
            #changed to return from notebook code
            return sel
            flag = 0
        else:
            print("invalid input")

#obtain file of selected currency
def obtainCurrencyRates(currency):
    if currency not in ratesForBase:
        return "invalid currency input"
    else:
        #code below is taken from example
        date = "2011-05-04"
        base = currency
        url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date}&base_currency_code={base}&format_type=xml"
        print(url)
        # Fetch the XML data
        response = requests.get(url)
        response.raise_for_status()  # Ensure we notice bad responses
        
        # Parse the XML data to a Python dictionary
        data_dict = xmltodict.parse(response.text)
        
        # Convert the dictionary to a JSON string
        json_data = json.dumps(data_dict, indent=4)
        
        # Print the JSON data
        print(json_data)
        
        # Optionally, write the JSON data to a file
        with open(f"{date}_exchange_rates_{base}.json", "w") as json_file:
            json_file.write(json_data)

try:
    select = selectCurrency()
except:
    print("problem in selectCurrency()")
try:
    obtainCurrencyRates(select)
except:
    print("problem in obtainCurrency()")