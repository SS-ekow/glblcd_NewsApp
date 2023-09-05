from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from newsapi import NewsApiClient




app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup")
def sign_up():
    return render_template("signup.html")



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)