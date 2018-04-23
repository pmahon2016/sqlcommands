import requests

import re


#this has been synced from my laptop




def get_abuse_status(myipadd ):
    
    response = requests.get("https://www.abuseipdb.com/check/"+ myipadd + "/json?key=IoGutYJumuBDzJkWq54qR5Mzpltpg3JjAUQ32JSY&days=30")
    
    if "country" in str(response.content):
    
        myList = str(response.content).split(',')
        print(myList[6] + myList[1] + myList[4])

#matchW = re.search('"isWhitelisted":false', str(response.content))


#this is from the imac compouter new new branch

get_abuse_status("10.191.195.186")


print(myList[6] + myList[1] + myList[4])




