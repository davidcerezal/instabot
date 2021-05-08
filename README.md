<p align="center">
    <img src="https://i.imgur.com/sJzfZsL.jpg" width="260" />
</p>

<h1 align="center">
  📷 Instagram + Python automation
</h1>

<p align="center">
   <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"/></a>
    <a href="https://www.python.org/downloads/release/python-370/"><img src="https://img.shields.io/badge/python-v3.7-blue" alt="Python v3.7"/></a>

</p>

<p align="center">
  Examples and improvement of <a href="https://instapy.org/">InstaPy</a> library
  <br />
  <br />
  Take a look, develop and take advance of that tool
  <br />
  <br />
  <a href="#table-of-contents"><strong>Explore the docs »</strong></a>
  <br />
  <br />
  <a href="https://github.com/davidcerezal/instabot/issues">Report Bug</a>
  ·
  <a href="https://github.com/davidcerezal/instabot/issues">Request Feature</a>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [🚀 Environment setup](#-environment-setup)
* [🤔 Project explanation](#-project-explanation)
  * [Starting example](#-ddd-skeleton)
  * [InstaBot Object](#-django-rest-framework)
  * [InstaBot Examples](#-django-rest-registration)
  * [Schedule Example](#-celery)
* [👷‍ Pro Tips](#-console-commands)
* [🤝 Contributing](#-contributing)

## 🚀 **Environment setup**
```elm
pip install instapy
```
__Important:__ depending on your system, make sure to use `pip3` and `python3` instead.


**That's it! 🚀**   
If you're on Ubuntu, read the specific guide on [Installing on Ubuntu (64-Bit)](https://github.com/InstaPy/instapy-docs/blob/master/How_Tos/How_To_DO_Ubuntu_on_Digital_Ocean.md). If you're on a Raspberry Pi, read the [Installing on RaspberryPi](https://github.com/InstaPy/instapy-docs/blob/master/How_Tos/How_to_Raspberry.md) guide instead.

>If you would like to install a specific version of Instapy you may do so with:
>```elm
>pip install instapy==0.1.1
>```

#### Running Instapy

To run InstaPy, you'll need to run the **[quickstart](https://github.com/InstaPy/instapy-quickstart)** script you've just downloaded.

- [Here is the easiest **quickstart** script you can use](https://github.com/InstaPy/instapy-quickstart/blob/master/quickstart.py)  

- [And here you can find lots of sophisticated **quickstart** templates shared by the community!](https://github.com/InstaPy/instapy-quickstart/tree/master/quickstart_templates) 

You can put in your account details now by passing the username and password parameters to the `InstaPy()` function in your **quickstart** script, like so: 
```python
InstaPy(username="abcd", 
        password="1234")
```
Or you can [pass them using the Command Line Interface (CLI)](/additional-information#pass-arguments-by-cli).

Once you have your **quickstart** script configured you can execute the script with the following commands.

```elm
python quickstart.py
-- or
python quickstart.py --username abcd --password 1234
```

InstaPy will now open a browser window and start working.

> If want InstaPy to run in the background pass the `--headless-browser` option when running from the CLI   
Or add the `headless_browser=True` parameter to the `InstaPy(headless_browser=True)` constructor.

#### Updating InstaPy
```elm
pip install instapy -U
```

## 🤔 Project explanation

This project tries to be a full rest API platform for Indexacapital.

###  Starting example

```elm
session = InstaPy(username=insta_username,
                  password=insta_password, 
                  headless_browser=True)
```

```elm
with smart_run(session):
```

```elm
session.set_user_interact(amount=3, randomize=True, percentage=80,media='Photo')
```

```elm
session.set_do_like(enabled=True, percentage=90)
```

```elm
session.like_by_tags(random.sample(like_tag_list, 3),
                    amount=random.randint(10, 20),interact=True)
```                         
###  InstaBot Object

```elm
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
```   


```elm
    logging.error('Login completed '+self.getTime()+' by '+self.name)
except:  
    logging.critical('Login failed '+self.getTime()+' by '+self.name)
```       

```elm
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
```               


###  InstaBot Examples


```elm  
def follow(self, list, number_of_users):

def follow_by_tags(self, list, number_of_users):

def follow_liker(self, list, number_of_users):

def comment(self, list, interactions):  

def unfollow(self, number_of_users): 

def like(self, list, interactions):       
```                      

```elm
from main import InstaBot

print( __file__)
bot = InstaBot('username', 'PASSXX', 'normal_follow')  

#Should execute every day at 10pm
#No more than 4 in (X*10*2 interactions)
bot.follow(['_chris_kap_', 'trasmispasos', 'algunandrea'], 10)
bot.end()
```   

      
###  Schedule Example
Bootstrap your new projects or be inspired by DDD and hexagonal architecture. 

```elm
import schedule
```   

```elm
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
 ```    



```elm
schedule.every().day.at("02:35").do(cron_unfollow)
schedule.every().day.at("10:35").do(cron_follow)
schedule.every().day.at("15:35").do(cron_like)
schedule.every().day.at("20:22").do(cron_follow)

while True:
  schedule.run_pending()
  time.sleep(10)
```     


## 👷‍ Pro Tips
Here are some tips that I adquired using this library, that maybe are helpfull for you (😜):

1. `Instagram` purpose is to have real user, so they will to punish any suspicious interaction. They already know that the easiest way to automate Instagram is through web, so they put an effort to track all actions through this platform.
2. As `Instagram` and us know that we use web platform to automate bots, they are constantly changing the web. From the other part, they are also updating the library. But **you should track your logs and bots almost every week to check if everything is working fine**.
3. `Instagram's` limit is over 100 integration / hour but the have accumulatives counters also. **Take care of reaching that limit in less than 2 hours.**
4. Developing this library creates a lot of integrations. **Do not try to develop with this library during a long time**. Distrubuting the development is better to minimize the access.
5. `Instagram` uses the IPs to check from where you are connecting. **Try to execute the bot from a server of same region. Also schedule your execution times in times that the account is used**. For example, if put a cron on a server of other region during the night, `Instagram` will know fast.
6. As my point of view, is better to put strong restriction rather than working with hug numbers. Try to get quality user rather than a lot users.

## 🤔 Contributing
There are some things missing (improve documentation...), feel free to add this if you want! If you want
some guidelines feel free to contact us :)

<a name="notRecommended">1</a>: This method is the slower and only must be used if you don't have connectivity with GitHub
