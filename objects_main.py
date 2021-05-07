from time import sleep
from instapy import InstaPy
from datetime import datetime
import logging

class InstaBot:
    def __init__(self, usr, pss, name):
        filename = name+'.log'
        logging.basicConfig(filename=filename)
        self.usr = usr
        self.name = name
        try:
            session = InstaPy(username=usr, password=pss)    
            session.login()
            self.bot = session
            self.bot.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
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
            logging.error('Login completed '+self.getTime()+' by '+self.name)
        except:  
            logging.critical('Login failed '+self.getTime()+' by '+self.name)

    def getSession(self):
        return self.bot   

    def getTime(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")      

    def follow(self, list, number_of_users):
        try:
            self.bot.set_skip_users(skip_no_profile_pic=True, skip_private=False)
            #self.bot.set_action_delays(enabled=True, like=5.2, randomize=True, random_range_from=70, random_range_to=140)
            self.bot.set_relationship_bounds(min_posts=10)
            #self.bot.set_user_interact(amount=2, percentage=100, randomize=True, media='Photo')
            self.bot.follow_user_followers(list, amount=number_of_users, randomize=True)
            logging.error('Follow completed '+self.getTime()+' by '+self.name)
        except:  
            logging.critical('Follow failed '+self.getTime()+' by '+self.name)

    def follow_by_tags(self, list, number_of_users):
        try:
            self.bot.set_skip_users(skip_no_profile_pic=True, skip_private=False)
            self.bot.set_action_delays(enabled=True, like=5.2, randomize=True, random_range_from=70, random_range_to=140)
            self.bot.set_relationship_bounds(potency_ratio=1.15, min_posts=10)
            self.bot.set_user_interact(amount=2, percentage=50, randomize=True, media='Photo')
            self.bot.session.follow_by_tags(list, amount=number_of_users, randomize=True, interact=True)
            logging.error('Follow by Tag completed '+self.getTime()+' by '+self.name)
        except:  
            logging.critical('Follow by Tag failed '+self.getTime()+' by '+self.name)  

    def follow_liker(self, list, number_of_users):
        try:
            self.bot.set_skip_users(skip_no_profile_pic=True, skip_private=False)
            self.bot.set_action_delays(enabled=True, like=5.2, randomize=True, random_range_from=70, random_range_to=140)
            self.bot.set_relationship_bounds(potency_ratio=1.15, min_posts=10)
            self.bot.set_user_interact(amount=2, percentage=50, randomize=True, media='Photo')
            self.bot.follow_likers(list, follow_likers_per_photo = number_of_users, randomize=True, interact=True)
            logging.error('Follow Liker completed '+self.getTime()+' by '+self.name)
        except:  
            logging.critical('Follow Liker failed '+self.getTime()+' by '+self.name)                

    def comment(self, list, interactions):
        try:
            self.bot.follow_user_followers(list, amount=number_of_users, randomize=True)
            logging.error('Comment completed '+self.getTime()+' by '+self.name)
        except:  
            logging.critical('Comment failed '+self.getTime()+' by '+self.name)

    def unfollow(self, number_of_users):
        try:
            self.bot.set_dont_unfollow_active_users(enabled=True, posts=3)
            self.bot.unfollow_users(amount=number_of_users, nonFollowers=True, style="LIFO", sleep_delay=60, unfollow_after=48*60*60)
            logging.error('Unfollow completed '+self.getTime()+' by '+self.name)
        except:  
            logging.critical('Unfollow failed '+self.getTime()+' by '+self.name)

    def like(self, list, interactions):
        try:
            #self.bot.set_action_delays(enabled=True, like=5.2, randomize=True, random_range_from=70, random_range_to=140)
            #self.bot.set_user_interact(amount=3, randomize=True, percentage=75, media='Photo')
            self.bot.like_by_tags(list, amount=interactions/3, randomize=True)
            logging.error('Like completed '+self.getTime()+' by '+self.name)
        except:  
            logging.critical('Like failed '+self.getTime()+' by '+self.name)

    def end(self):
        self.bot.end(threaded_session=True)