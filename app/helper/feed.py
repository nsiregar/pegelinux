import feedparser
import datetime
from app import db
from app.models.post import Post
from app.models.feed import Feed, APPROVED


def get_feed(url):
    try:
        feeds = feedparser.parse(url)
        return feeds.get('status'), feeds.entries
    except Exception as e:
        msg = f'Error {e} occured'
        print(msg)

def parse_feed():
    urls = Feed.query.filter_by(approved=APPROVED).all()
    for url in urls:
        print(f'Trying to parse RSS from { url.rss }')
        status_code, entries = get_feed(url.rss)
        if status != 200:
            print(f'Status code {status_code} for {url.rss}')
            continue

        for item in entries:
            pubtime = datetime.datetime(*(item.published_parsed[0:7]))
            record = Post.query.filter_by(url=item.link).first()
            if record is None:
                save_post(item, pubtime, url)

def save_post(item, pubtime, url):
    post = Post(
        title=item.title,
        url=item.link,
        date=pubtime,
        owner=url.owner,
        domain=url.html,
    )
    db.session.add(post)
    db.session.commit()
    print('News added from { item.link }')
