from newspaper import Article
from bs4 import BeautifulSoup
import requests


no_duplicates = set()
with open('output.txt') as file:
	for line in file:
		no_duplicates.add(line)#makes sure article urls dont repeat


location_frequency=[]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36"
} # so it looks like a normal request 


for url in no_duplicates:

	try:
		response = requests.get(url, headers=headers,timeout=10)
		if response.status_code == 200:
			print(f"Download succeeded: {url}")
			soup = BeautifulSoup(response.text, 'html.parser')
			#using a regualr for loop search "wisoncsin" in article.text
			#in the per article section for list once 
			#use a list for state names 
			#count number of occurences across all artciles and make into a map to use colors 

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

			text = soup.get_text(" ", strip=True)
			for state in state_names:
				if state in text:
					location_frequency.append(state)
			
			print(location_frequency)
		else:
			print(f"Download failed ({response.status_code}): {url}")
	except requests.RequestException as e:
		print(f"Download failed: {e}")

	
	








	
















	









		
		
	










		
		
		