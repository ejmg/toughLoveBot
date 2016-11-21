"""
a bot that tweets tough love (and some non-sense humor)

author: elias g. and elliot p.
version: 21.11.16
"""
import tweepy as ty
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
    return apy

if __name__ == "__main__":
    api = setTwitterAuth()
    print("Gabby is the best") 
