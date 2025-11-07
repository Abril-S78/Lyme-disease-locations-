from newspaper import Article




no_duplicates = set()
with open('output.txt') as file:
	for line in file:
		no_duplicates.add(line)#makes sure article urls dont repeat


location_frequency=[]


for url in no_duplicates:
	article = Article(url)
	article.download()

	try:
		article.download()
		if article.download_state == 1:
			print(f"Download succeeded: {url}")
			article.parse() 
			#using a regualr for loop search "wisoncsin" in article.text
			#in the per article section for list once 
			#use a list for state names 
			#count number of occurences across all artciles and make into a map to use colors 

			state_names=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

			



			for state in state_names:
				if state in article.text:
					location_frequency.append(state)
			
			print(location_frequency)
		else:
			print(url+"Download failed!")
	except Exception as e:
		print(f"Error with {url}: {e}")

	
	








	
















	









		
		
	










		
		
		