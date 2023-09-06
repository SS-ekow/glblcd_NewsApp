import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
apiKey = os.environ.get("apiKey")


if apiKey is None:
    raise Exception("API key not found. Make sure to set it in your .env file.")


base_url = "https://newsapi.org/v2/top-headlines"
params = {"country": "ghana",
          "category": "business", 
          "apiKey": apiKey}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    articles = data.get("articles")


    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"Source: {article['source']['name']}")
        print(f"Published At: {article['publishedAt']}")
        print(f"URL: {article['url']}")
        print("\n")
    
    

else:
    print(f"Error: {response.status_code} - {response.text}")


