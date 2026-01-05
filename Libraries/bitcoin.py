import requests
import sys
import json

def main():
    amount = validateCliInput()
    total_cost = obtainNumber(amount)
    print(f"${total_cost:,.4f}")





def validateCliInput():
    try: # try - potential value error or IndexError 
        number_of_btc = float(sys.argv[1]) # the argument from CLI
    except ValueError:
        sys.exit("Command-line argument is not a float")
    except IndexError:
        sys.exit("Missing command-line argument")

    return number_of_btc

def obtainNumber(number_of_btc):
    # here is where I should make the request and format it
    # it should return a numbered value that's formatted
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=ac1847e41663a3a3e8a3d734928d86d6ad0cc8d2eabde9fbd85a5db48e8bdc62")
    except requests.RequestException:
        sys.exit('Invalid request')
    # formatting for python
    response = response.json()
    
    price = float(response["data"]["priceUsd"]) * number_of_btc
    return price




main()
