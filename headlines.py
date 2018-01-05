import feedparser

from flask import Flask
from flask import render_template


app = Flask(__name__)

FEEDS = {'mail': "https://news.mail.ru/rss",
         'ntv': "https://www.ntv.ru/exp/newsrss_top.jsp"}


@app.route("/")
@app.route("/<publication>")
def get_news(publication='mail'):
    feed = feedparser.parse(FEEDS[publication])
    first_article = feed['entries'][0]
    return render_template("home.html",
                           title=first_article.get("title"),
                           published=first_article.get("published"),
                           summary=first_article.get("summary"))


if __name__ == "__main__":
    app.run(port=5000, debug=True)
