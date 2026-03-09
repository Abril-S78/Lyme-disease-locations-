#Specifies the type of articles Im looking for 

from newspaper import Article
from bs4 import BeautifulSoup
import requests

total = 0 
lyme =0

# no duplicate articles using a set 
no_duplicates = set()
with open('output.txt') as file:
    for x in file:
        no_duplicates.add(x.strip())
        total+=1



location_frequency = {}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36"
}

state_names = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
    "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

# finds lowercase names 
state_names = [state.lower() for state in state_names]

for url in no_duplicates:

    #filter urls 
    if not any(keyword in url.lower() for keyword in ["lyme"]):
        continue

    try:
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code == 200:
            print(f"Download succeeded: {url}")

            soup = BeautifulSoup(response.text, 'html.parser')

            text = soup.get_text(" ", strip=True).lower()
           
            words = text.split()

            for i in range(len(words)):

                #one word 
                if words[i] in state_names:
                    if words[i] in location_frequency:
                        location_frequency[words[i]] += 1
                    else:
                        location_frequency[words[i]] = 1

                # two words 
                if i < len(words) - 1:
                    two_word = words[i] + " " + words[i+1]
                    if two_word in state_names:
                        if two_word in location_frequency:
                            location_frequency[two_word] += 1
                        else:
                            location_frequency[two_word] = 1
            lyme +=1

        else:
            print(f"Download failed ({response.status_code}): {url}")

    except requests.RequestException as e:
        print(f"Download failed: {e}")

print(location_frequency)
Frequency = "Frequency of lyme articles: ",lyme,"/",total







	









		
		
	










		
		
		
