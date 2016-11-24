"""
a bot that tweets tough love (and some non-sense humor)

author: elias g. and elliot p.
version: 21.11.16
"""
import tweepy as ty
import arrow
import random
from toughLoveTweets import (tweets, worriedReplies, lonelyReplies,
                             sickReplies)
from toughLoveSecret import (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
                             ACCESS_SECRET)


# testing out api stuff before moving on...
def deleteOldTweets(api, tweet):
    """
    delete any any tweet that is a duplicate of the tweet in the last
    96 tweets. 4 tweets each hour per 24 hours = 96 tweets
    """
    oldTweets = api.user_timeline("@TOUGHLOVEBOT", count=96)
    for old in oldTweets:
        if old.text == tweet:
            api.destroy_status(old.id)


def setTwitterAuth():
    """
    obtains authorization from twitter API
    """
    # sets the auth tokens for twitter using tweepy
    auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api


def sendTweet(api):
    """
    selects a psuedo-random tweet from the tweets list, checks for duplicates,
    and tweets the message.
    """
    tweet = tweets[random.randint(0, len(tweets) - 1)]
    deleteOldTweets(api, tweet)
    api.update_status(tweet)

# driver is testing out stuff rn, not for deployment
if __name__ == "__main__":
    # get yesterday's date, this time
    time = arrow.now("US/Central").replace(days=-1).format("D HH:mm")
    api = setTwitterAuth()
    if time[-2::] == "00" or time[-2::] == "30":
        sendTweet(api)
    # me = api.me()
    # print(dir(me))
    # print(me.id)
    # deleteOldTweets(api)
    
    # tweet = ""
    # api.update_status()
