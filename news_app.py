from flask import Flask, render_template
from newsapi import NewsApiClient
from forms import RegistrationForm


newsapi = NewsApiClient(api_key='dafcceb89a5f4a39a8772cae8649c766')




app = Flask(__name__)



@app.route("/")
def home():
   
    response = newsapi.get_top_headlines(language='en', country='us')  
    
    all_articles = newsapi.get_everything(sources='bbc-news,the-verge', domains='bbc.co.uk,techcrunch.com', from_param='2023-08-10', to='2023-09-06', language='en', sort_by='relevancy', page=2)
    
    
 
     
    return render_template("home.html",  response=response, all_articles=all_articles)

    







@app.route("/signup")
def register():
    form = RegistrationForm()
    
    return render_template('signup.html', title='Register', form=form)



@app.route("/category/<cat>")
def category(cat):
    
    response = newsapi.get_top_headlines(language='en', country='us')
    
    category_list = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']
    if cat in category_list:
        top_headlines = newsapi.get_top_headlines(category=cat, language='en', country='us', page=2)
        return render_template("category.html", top_headlines=top_headlines, response=response)
    
      
    
    
    return render_template("category.html")

# @app.route("/search")
# def search():
    
#     return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)