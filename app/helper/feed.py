import feedparser
import datetime
from app import db
from app.models.post import Post
from app.models.feed import Feed, APPROVED


def parseFeed(url):
    return feedparser.parse(url)


def getFeed():
    urls = Feed.query.filter_by(approved=APPROVED).all()
    for url in urls:
        feed = parseFeed(url.rss)
        if feed.status == 301:
            return 'feed redirected please update to new feed'
        if feed.status == 410:
            return 'feed is gone'
        if feed.status == 404:
            return 'feed not found'
        for item in feed.entries:
            pubtime = datetime.datetime(*(item.published_parsed[0:7]))
            record = Post.query.filter_by(url=item.link).first()
            if record is None:
                post = Post(
                    title=item.title,
                    url=item.link,
                    date=pubtime,
                    owner=url.owner,
                    domain=url.html,
                )
                db.session.add(post)
                db.session.commit()
                print("News added from {}".format(item.link))
