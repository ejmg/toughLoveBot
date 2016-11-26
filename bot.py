"""
a bot that tweets tough love (and some non-sense humor)

author: elias g. and elliot p.
version: 21.11.16
"""
import tweepy as ty
import arrow
import random
from toughLoveTweets import (statusTweets, worriedReplies, lonelyReplies,
                             sickReplies, followerReplies)
from toughLoveSecret import (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
                             ACCESS_SECRET, ID)


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


def getSearch(api, search):
    """
    gets search results of the string, search, returns 100 tweets.
    """
    searchResults = [status for status in ty.
                     Cursor(api.search, q=search).items(100)]
    return searchResults


def tweetAtFollower(api, bot):
    """
    this method chooses a random follower to tweet a positive message at.
    """
    # Choose the random tweet and prepare it for the user to be selected
    message = followerReplies[random.randint(0, len(followerReplies) - 1)]
    tweet = ".@{} " + message

    # create normal list from cursor list for the sake of making randomly
    # selecting a user easier
    followers = [follower for follower in ty.Cursor(api.followers).items()]
    randomFollower = followers[random.randint(0, len(followers) - 1)]
    # get the user handle from the random follower chosen
    followerHandle = randomFollower.screen_name
    # check for duplicate, tweet away!
    deleteOldTweets(api, tweet.format(followerHandle))
    api.update_status(tweet.format(followerHandle))


def replyRandomTweet(api):
    randInt = randInt(0, 2)
    if randInt == 0:
        search = "\"I am sad\""
        searchResults = getSearch(api, search)
        
    elif randInt == 1:
    elif randInt == 2:


def sendTweet(api):
    """
    selects a psuedo-random tweet from the tweets list, checks for duplicates,
    and tweets the message.
    """
    tweet = statusTweets[random.randint(0, len(statusTweets) - 1)]
    deleteOldTweets(api, tweet)
    api.update_status(tweet)


# driver is testing out stuff rn, not for deployment
if __name__ == "__main__":
    # get yesterday's date, this time
    time = arrow.now("US/Central").replace(days=-1).format("D HH:mm")
    api = setTwitterAuth()
    bot = api.me()
    if time[-2::] == "00":
        sendTweet(api)
    elif time[-2::] -== "30":
        send
    # me = api.me()
    # print(dir(me))
    # print(me.id)
    # deleteOldTweets(api)
    
    # tweet = ""
    # api.update_status()
