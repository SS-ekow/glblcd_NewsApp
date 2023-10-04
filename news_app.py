from flask import Flask, render_template, request, jsonify
import requests
from newsapi import NewsApiClient

import secret_keys

newsapi = NewsApiClient(api_key= secret_keys.apiKey)



app = Flask(__name__)

app.config['SECRET_KEY'] = secret_keys.secret_key



@app.route("/")
def home():
   
    response = newsapi.get_top_headlines(language='en', country='us', page = 2)  
    
    all_articles = newsapi.get_everything(sources='bbc-news,the-verge', domains='bbc.co.uk,techcrunch.com', language='en', sort_by='relevancy', page=2)
    
    
 
     
    return render_template("home.html",  response=response, all_articles=all_articles)

    







@app.route("/signup")
def register():
    
    
    return render_template('signup.html', title='Register')



@app.route("/category/<cat>")
def category(cat):
    
    response = newsapi.get_top_headlines(language='en', country='us')
    
    category_list = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']
    if cat in category_list:
        top_headlines = newsapi.get_top_headlines(category=cat, language='en', country='us', page=2)
        return render_template("category.html", top_headlines=top_headlines, response=response)
    
      
    
    
    return render_template("category.html")

@app.route("/search", methods=['GET', 'POST'])
def search():
    
    # keyword = request.form.get('keyword')
    
    url = ('https://newsapi.org/v2/everything?'
       'q=bitcoin&'
       'sources=bbc-news&'
        'domains=bbc.co.uk&'
       'from_param=2023-09-01&'
       'to=2023-09-11&'
       'sortBy=popularity&'
       'apiKey=9a7b975fbe1a468a93b12f0d6b9fce57')

    response = requests.get(url)

  
    
    return render_template("search.html", response=response)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    