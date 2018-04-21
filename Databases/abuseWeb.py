import requests
import re

response = requests.get("https://www.abuseipdb.com/check/51.144.121.104/json?key=IoGutYJumuBDzJkWq54qR5Mzpltpg3JjAUQ32JSY&days=30")

print(response.content)

myList = str(response.content).split(',')

matchW = re.search('"isWhitelisted":false', str(response.content))

print(myList[6] + myList[1] + myList[4])

