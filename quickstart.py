""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'allyberguist'
insta_password = 'IGColin1021'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

# let's go! :>
with smart_run(session):
    hashtags = ['plants', 'plant', 'mountains',
                'forest',
                'reflections', 'nofilter', 'hiking',
                'reflection', 'garden',
                'trees', 'indoorplants', 'beautifuldestinations',
                'tulips',
                'orchids', 'houseplants', 'neature', 'sunset',
                'tropicalplants',
                'igtravel', 'ighouseplants', 'plantsofinstagram', 'instaplants',
                'flowering',
                'petals', 'sky', 'leaves', 'sunrise',
                'blooms', 'travel',
                'sunset_pics', 'vacation', 'ocean',
                'photographyoftheday', 'macrophotography',
                'explorenature', 'sea', 'hike',
                'landscape', 'macro',
                'flowers', 'igplants', 'ig_nature', 'nature',
                'flower']
    random.shuffle(hashtags)
    my_hashtags = hashtags[:10]

    # general settings
    session.set_dont_like(['sex', 'weed', 'gun','porn', 'nude', 'god','lgbt', 'gay', 'stoner'])
    session.set_do_follow(enabled=True, percentage=10, times=1)
    session.set_do_comment(enabled=True, percentage=30)
    session.set_comments([
                             u'Amazing shot! :heart_eyes: :heart_eyes:',
                             u'This is my new favorite! :heart_eyes:',
                             u'So lovely! :heart_eyes: :heart_eyes:',
                             u'Wonderful!! :smiley:',
                             u'This is awesome!! :heart_eyes:',
                             u'Amazing!! :heart_eyes:',
                             u'I really like the way you captured this!',
                             u'Cool shot! :smiley: :smiley:',
                             u'Great capture!! :smiley: :smiley:',
                             u'Wow - this is great! :heart_eyes: :smiley: :heart_eyes:'],
                         media='Photo')
    session.set_do_like(True, percentage=70)
    session.set_delimit_liking(enabled=True, max=100, min=0)
    session.set_delimit_commenting(enabled=True, max=100, min=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=5000,
                                    max_following=2000,
                                    min_followers=100,
                                    min_following=50)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "follows"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes=(100, 1000),
                                 peak_comments=(21, 250),
                                 peak_follows=(200, None))

    session.set_user_interact(amount=1, randomize=False, percentage=40)

    # activity
    session.like_by_tags(my_hashtags, amount=600, media=None)
    session.unfollow_users(amount=0, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=501)
    session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=501)

    """ Joining Engagement Pods...
    """
    session.join_pods()

