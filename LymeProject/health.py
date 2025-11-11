#Abril Sifuentes 
#09/14/25 
# Lyme disease search  project 
#steps----------------------
#url': 'https://www.naturalnews.com/2025-08-20-just-like-that-the-massive-measles-plandemic-2025-is-over.html', 
# all I need to do is extract these links and out then into a list. 
# Then have each article run through newspaper api to extract text and 
# then use  python library to extract locations in text.
#then count the frequency of these locations listed and put them on a matplotlib chart
#--------------------------------------

from newsapi import NewsApiClient

#call on api with my own user key 
newsapi = NewsApiClient(api_key='b68a395592224969800fe410be62e1c5')




#documentation with my own spin on the query
# fetch all articles about Lyme disease
headlines = newsapi.get_everything(q='lyme disease', language='en', page_size=100)

#opens a txt file while only reading the urls into the txt file 
with open("output.txt","a") as f:
	for line in headlines['articles']:
	    print(line['url'],file =f) #extracts urls 
f.close()


#google scheudler for intro into cloud computing daily api update once






		



    







	