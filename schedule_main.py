from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import schedule
import logging
import time

filename = 'xxxxx.log'
logging.basicConfig(filename=filename)

def cron_follow():
  session = InstaPy(username='xxxx', password='passs',headless_browser=True)    
  session.login()
  session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
    peak_likes_hourly=80,
    peak_likes_daily=None,
    peak_comments_hourly=30,
    peak_comments_daily=None,
    peak_follows_hourly=80,
    peak_follows_daily=None,
    peak_unfollows_hourly=80,
    peak_unfollows_daily=None,
    peak_server_calls_hourly=None,
    peak_server_calls_daily=4700)
  session.follow_user_followers(['relatosencontrados8', 'trasmispasos', 'algunandrea'], amount=10, randomize=True)
  session.end()

def cron_like():
  session = InstaPy(username='xxxx', password='passs',headless_browser=True)     
  session.login()
  session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
    peak_likes_hourly=80,
    peak_likes_daily=None,
    peak_comments_hourly=30,
    peak_comments_daily=None,
    peak_follows_hourly=80,
    peak_follows_daily=None,
    peak_unfollows_hourly=80,
    peak_unfollows_daily=None,
    peak_server_calls_hourly=None,
    peak_server_calls_daily=4700)
  session.like_by_tags(['relatos', 'instarelatos', 'reflexiones'], amount=10, randomize=True)
  session.end()

def cron_unfollow():
  session = InstaPy(username='xxxx', password='passs',headless_browser=True)    
  session.login()
  session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
    peak_likes_hourly=80,
    peak_likes_daily=None,
    peak_comments_hourly=30,
    peak_comments_daily=None,
    peak_follows_hourly=80,
    peak_follows_daily=None,
    peak_unfollows_hourly=80,
    peak_unfollows_daily=None,
    peak_server_calls_hourly=None,
    peak_server_calls_daily=4700)
  session.unfollow_users(amount=40, nonFollowers=True, style="LIFO", sleep_delay=60, unfollow_after=48*60*60)
  session.end()


schedule.every().day.at("02:35").do(cron_unfollow)
schedule.every().day.at("10:35").do(cron_follow)
schedule.every().day.at("15:35").do(cron_like)
schedule.every().day.at("20:22").do(cron_follow)

while True:
  schedule.run_pending()
  time.sleep(10)