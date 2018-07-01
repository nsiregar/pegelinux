import time
import atexit
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from app import app
from app.helper.feed import getFeed


@app.before_first_request
def init():
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(
        func=getFeed,
        trigger=IntervalTrigger(minutes=30),
        id="get_rss_fed",
        name="Get Feed every 30 minutes",
        replace_existing=True,
    )
    atexit.register(lambda: scheduler.shutdown())


logging.basicConfig()
logging.getLogger("apscheduler").setLevel(logging.DEBUG)
