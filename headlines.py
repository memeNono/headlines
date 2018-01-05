import feedparser
from flask import Flask


app = Flask(__name__)

FEEDS = {'mail': "https://news.mail.ru/rss",
         'ntv': "https://www.ntv.ru/exp/newsrss_top.jsp"}


@app.route("/")
@app.route("/<publication>")
def get_news(publication='mail'):
    feed = feedparser.parse(FEEDS[publication])
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1> Новости </h1>
                <b>{0}</b> <br/>
                <i>{1}</i> <br/>
                <p>{2}</p> <br/>
        </body>
    </html>""".format(first_article.get("title"),
                      first_article.get("published"),
                      first_article.get("summary"))


if __name__ == "__main__":
    app.run(port=5000, debug=True)
