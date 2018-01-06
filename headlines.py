import feedparser

from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
         'ntv': "https://www.ntv.ru/exp/newsrss_top.jsp"}


@app.route("/",methods=['GET','POST'])
def get_news():
    query = request.form.get("publication")
    if not query or query.lower() not in FEEDS:
        publication = 'bbc'
    else:
        publication = query.lower()
    feed = feedparser.parse(FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])


if __name__ == "__main__":
    app.run(port=5000, debug=True)
