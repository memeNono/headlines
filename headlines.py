import feedparser

from flask import Flask
from flask import render_template


app = Flask(__name__)

FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
         'ntv': "https://www.ntv.ru/exp/newsrss_top.jsp"}


@app.route("/")
@app.route("/<publication>")
def get_news(publication='bbc'):
    feed = feedparser.parse(FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])


if __name__ == "__main__":
    app.run(port=5000, debug=True)
