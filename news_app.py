from flask import Flask, render_template
from newsapi.newsapi_client import NewsApiClient

newsapi = NewsApiClient(api_key='9a7b975fbe1a468a93b12f0d6b9fce57')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup")
def sign_up():
    return render_template("signup.html")

@app.route("/category/<cat>")
def category(cat):
    
    category_list = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']
    if cat in category_list:
        top_headlines = newsapi.get_top_headlines(category=cat, language='en', country='us')
        return render_template("category.html", top_headlines=top_headlines)
    
    return render_template("category.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    