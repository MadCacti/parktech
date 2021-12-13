# import "packages" from flask
import json
from flask import Flask, render_template, request
from newsapi.newsapi_client import NewsApiClient
import requests
import firebase_admin
from firebase_admin import credentials
# create a Flask instance
app = Flask(__name__)


yourAPIKEY = '8169dc4f99474483ab5999bc2c761381'  # write your API key here
newsapi = NewsApiClient(api_key=yourAPIKEY)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/raiden/')
def raiden():
    return render_template("profiles/raiden.html", news='')


@app.route('/raiden/results/', methods=['POST'])
def get_results():
    keyword = request.form['keyword']  # getting input from user

    news = newsapi.get_top_headlines(q=keyword,
                                     # sources='bbc-news,the-verge',#optional and you can change
                                     # category='business', #optional and you can change also
                                     language='en',  # optional and you can change also
                                     country='in')
    # print(news['articles'])
    return render_template('profiles/raiden.html', news=news['articles'])


@app.route('/paul/')
def paul():
    return render_template("profiles/paul.html")


@app.route('/armaan/')
def armaan():
    return render_template("profiles/armaan.html")


@app.route('/API/')
def API():
    return render_template("profiles/API.html")


@app.route('/kurtis/')
def kurtis():

    url = "https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia"
    querystring = {"category":"sciencenature","limit":"1"}
    headers = {
        'x-rapidapi-host': "trivia-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "6279ac9b7amsh7dc015c7d7746fbp1f4d65jsn125b0c500438"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    output = json.loads(response.text)
    return render_template("profiles/kurtis.html", question=output)
# runs the application on the development server


@app.route('/rating_test/')
def rating_test():
    return render_template("ratings/rating_test.html")


@app.route('/five_stars/')
def five_stars():
    return render_template("ratings/five_stars.html")


@app.route('/four_stars/')
def four_stars():
    return render_template("ratings/four_stars.html")


@app.route('/three_stars/')
def three_stars():
    return render_template("ratings/three_stars.html")


@app.route('/two_stars/')
def two_stars():
    return render_template("ratings/two_stars.html")


@app.route('/one_star/')
def one_star():
    return render_template("ratings/one_star.html")


@app.route('/databases/')
def databases():
    return render_template("Databases/databases.html")


@app.route('/search/')
def search():
    return render_template("search.html")


@app.route('/database1/')
def database1():
    return render_template("Databases/database1.html")


@app.route('/login/', methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route('register')
def register():
    return render_template("register.html")


@app.route('error')
def error():
    return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)
