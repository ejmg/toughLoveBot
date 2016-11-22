"""
a bot that tweets tough love (and some non-sense humor)

author: elias g. and elliot p.
version: 21.11.16
"""
import tweepy as ty
from toughLoveTweets import (tweets, worriedReplies, lonelyReplies,
                             sickReplies)
from toughLoveSecret import (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
                             ACCESS_SECRET)

# testing out api stuff before moving on...
def getLast20Tweets(api):
    last20 = api.user_timeline()
    for oldtweet in last20:
        print(oldtweet.text)


def setTwitterAuth():
    """
    obtains authorization from twitter API
    """
    # sets the auth tokens for twitter using tweepy
    auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api

# driver is testing out stuff rn, not for deployment
if __name__ == "__main__":
    api = setTwitterAuth()
    me = api.me()
    print(dir(me))
    print(me.id)
    getLast20Tweets(api)
    # tweet = ""
    # api.update_status()
