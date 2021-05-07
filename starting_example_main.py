import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username ='USer'
insta_password = 'PASSXX'

# restriction data

# TARGET data
""" Set similar accounts and influencers from your niche to target...
"""
like_tag_list = ['instarelatos', 'relatos', 'instatail', 'relatoscortos',
                 'relatosdebolsillo', 'cuentorapido', 'microrelato',
                 'microcuento']º
targets = ['ferialibromadrid', 'trasmispasos', 'algunandrea']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password, 
                  headless_browser=True)
# let's go! :>
with smart_run(session):
    # HEY HO LETS GO
    # general settings
    session.set_simulation(enabled=True)

    session.set_user_interact(amount=3, randomize=True, percentage=80,
                              media='Photo')
    session.set_do_like(enabled=True, percentage=90)
    session.set_do_follow(enabled=True, percentage=40, times=1)

    # activities
   # FOLLOW+INTERACTION on TARGETED accounts
    """ Select users form a list of a predefined targets...
    """
    number = random.randint(3, 5)
    random_targets = targets

    if len(targets) <= number:
        random_targets = targets

    else:
        random_targets = random.sample(targets, number)

    """ Interact with the chosen targets...
    """
    session.follow_user_followers(random_targets,
                                  amount=random.randint(10, 20),
                                  randomize=True, sleep_delay=700,
                                  interact=True)

    # activity
    session.like_by_tags(random.sample(like_tag_list, 3),
                         amount=random.randint(10, 20), interact=True)

    # UNFOLLOW activity
    """ Unfollow nonfollowers after one day...
    """
    session.unfollow_users(amount=random.randint(75, 100),
                           nonFollowers=True,
                           style="FIFO",
                           unfollow_after=2 * 24 * 60 * 60, sleep_delay=600)

    """ Unfollow all users followed by InstaPy after one week to keep the
    following-level clean...
    """
    session.unfollow_users(amount=random.randint(75, 100),
                           allFollowing=True,
                           style="FIFO",
                           unfollow_after=7 * 24 * 60 * 60, sleep_delay=600)