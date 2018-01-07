import feedparser
import json
import urllib.parse
import urllib.request

from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

DEFAULTS = {'publication': "bbc",
            'city': "London,UK"}

FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
         'ntv': "https://www.ntv.ru/exp/newsrss_top.jsp"}


@app.route("/")
def home():
    publication = request.args.get('publication')
    if not publication:
        publication = DEFAULTS['publication']
    articles = get_news(publication)
    city = request.args.get('city')
    if not city:
        city = DEFAULTS['city']
    weather = get_weather(city)
    return render_template("home.html", articles=articles, weather=weather)


def get_news(query):
    if not query or query.lower() not in FEEDS:
        publication = 'bbc'
    else:
        publication = query.lower()
    feed = feedparser.parse(FEEDS[publication])
    return feed['entries']


def get_weather(query):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}" \
            "&units=metric&appid=c3c13229692eb0f40b50aa542cd015eb"
    query = urllib.parse.quote(query)
    url = api_url.format(query)
    data = urllib.request.urlopen(url).read().decode("utf-8")
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {"description":
                   parsed["weather"][0]["description"],
                   "temperature": parsed["main"]["temp"],
                   "city": parsed["name"],
                   "country": parsed["sys"]["country"]
                   }
    return weather


if __name__ == "__main__":
    app.run(port=5000, debug=True)
