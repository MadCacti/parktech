# import "packages" from flask
from flask import Flask, render_template, request
from newsapi.newsapi_client import NewsApiClient
import requests
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


@app.route('/kurtis/')
def kurtis():
    return render_template("profiles/kurtis.html")
# runs the application on the development server


if __name__ == "__main__":
    app.run(debug=True)
