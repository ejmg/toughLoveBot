import tweepy as ty
import arrow
import random
from toughLoveTweets import (tweets, worriedReplies, lonelyReplies,
                             sickReplies)
from toughLoveSecret import (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
                             ACCESS_SECRET)


def setTwitterAuth():
    """
    obtains authorization from twitter API
    """
    # sets the auth tokens for twitter using tweepy
    auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api


def getFollowers(api):
    followers = ty.Cursor(api.followers).items()
    for follower in followers:
        print(follower.name)

def getSearch(api, search):
    searchResults = api.search(search)
    for result in searchResults:
        print(result.text)

if __name__ == "__main__":
    api = setTwitterAuth()
    # getSearch(api, "\"I am sad\"")
    getFollowers(api)
