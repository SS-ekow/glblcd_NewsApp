from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from newsapi import NewsApiClient
from forms import RegistrationForm

newsapi = NewsApiClient(api_key='9a7b975fbe1a468a93b12f0d6b9fce57')




app = Flask(__name__)

app.config['SECRET_KEY'] = '55af5c09aad400be122a'

@app.route("/")
def home():
   
    response = newsapi.get_top_headlines(language='en', country='us')   
     
    return render_template("home.html",response=response)

    







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
    
    else:
        flash("Category does not exist. (for this api.)")
    
    
    
    return render_template("category.html")




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)