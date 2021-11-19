# import "packages" from flask
from flask import Flask, render_template, request
#from newsapi.newsapi_client import NewsApiClient
import requests
# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/raiden/')
def raiden():
    return render_template("profiles/raiden.html")


@app.route('/paul/')
def paul():
    return render_template("profiles/paul.html")


@app.route('/armaan/')
def armaan():
    return render_template("profiles/armaan.html")


@app.route('/kurtis/')
def kurtis():
    return render_template("profiles/kurtis.html")
# runs the application on the development server


if __name__ == "__main__":
    app.run(debug=True)
