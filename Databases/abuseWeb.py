import requests



#url = "https://www.abuseipdb.com/check/111.161.35.146/json?key=IoGutYJumuBDzJkWq54qR5Mzpltpg3JjAUQ32JSY&days=30"

response = requests.get("https://www.abuseipdb.com/check/111.161.35.146/json?key=IoGutYJumuBDzJkWq54qR5Mzpltpg3JjAUQ32JSY&days=30")

print(response.content)