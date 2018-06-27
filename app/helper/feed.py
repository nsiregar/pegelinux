import feedparser
import datetime
from app import db
from app.models.post import Post

blogs = {
    'mimin': {
        'rss': 'https://www.rizaumami.com/index.xml',
        'html': 'https://www.rizaumami.com'
    },
    'situsali': {
        'rss': 'https://situsali.com/feed/',
        'html': 'https://situsali.com'
    },
    'kabarlinux': {
        'rss': 'https://kabarlinux.id/feed/',
        'html': 'https://kabarlinux.id'
    },
    'bang hamid': {
        'rss': 'https://ahmadihamid.com/feed.xml',
        'html': 'https://ahmadihamid.com'
    },
    'catatan kecil': {
        'rss': 'https://ha.hn.web.id/feed/',
        'html': 'https://ha.hn.web.id'
    },
    'kertas kecil': {
        'rss': 'https://bluemeda.web.id/rss/',
        'html': 'https://bluemeda.web.id'
    },
    'cak aries': {
        'rss': 'https://blog.arsmp.com/feed/',
        'html': 'https://blog.arsmp.com'
    },
    'bang rejha': {
        'rss': 'https://rezhajulio.id/index.xml',
        'html': 'https://rezhajulio.id'
    }
}

def parseFeed(url):
    return feedparser.parse(url)

def getFeed():
    for key, url in blogs.items():
        for item in parseFeed(url['rss']).entries:
            pubtime = datetime.datetime(*(item.published_parsed[0:7]))
            try:
                post = Post(title=item.title, url=item.link, date=pubtime, owner=key, domain=url['html'])
                db.session.add(post)
                db.session.commit()
            except Exception:
                pass