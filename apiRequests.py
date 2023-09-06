import requests
# from pprint import pprint

from newsapi import NewsApiClient
api_key= 'e03943ee0ea8443f95e6e4a671c85ccc'
newsapi =  NewsApiClient(api_key)

# if newsapi is None:
#     raise Exception("API key not found. Make sure to set it in your .env file.")


top_headlines = newsapi.get_top_headlines(q = "",
                                          category = "general",
                                          language='en',
                                          country = "au")


# all_articles = newsapi.get_everything(q='bitcoin',
#                                     #   sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2023-08-06',
#                                       to='2023-09-05',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)


# base_url = "https://newsapi.org/v2/top-headlines"
# params = {"country": "ghana",
#           "category": "business", 
#           "apiKey": api_key}

# response = requests.get(base_url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     articles = data.get("articles")


for article in top_headlines['articles']:
    print(f"Title: {article['title']}")
    print(f"Description: {article['description']}")
    print(f"Source: {article['source']['name']}")
    print(f"Published At: {article['publishedAt']}")
    print(f"URL: {article['url']}")
    print("\n")
    
    

# else:
#     print(f"Error: {response.status_code} - {response.text}")


