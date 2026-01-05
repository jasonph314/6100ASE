import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1]) 

data = response.json()


for result in data["results"]:
    print(f"{result['trackName']} by {result['artistName']}")
