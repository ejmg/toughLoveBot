# -*- coding: utf-8 -*-

import tweepy as ty
import json
from toughLoveSecret import (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
                             ACCESS_SECRET)
from toughLoveTweets import followerReplies
import random

#override tweepy.StreamListener class
class DaysStreamListener(ty.StreamListener):

    def __init__(self, api):
        self.api = api
        super(ty.StreamListener, self).__init__()

    def on_data(self, data):
        data = json.loads(data)
        self.respond(data)

    def on_error(self, status):
        print(status)

    def respond(self, data): 
        """
        method to respond to a tweet directed at @toughlovebot
        """
        user = data['user']['screen_name']
        #print(user)
        #avoid getting into an infinite loop with the bot at all costs
        if user == 'TOUGHLOVEBOT': 
            return 
        tweet_id = data['id']
        
        reply = followerReplies[random.randint(0, len(followerReplies) - 1)]
        reply_tweet = "@{} " + reply
        reply_tweet = reply_tweet.format(user)
        api.update_status(status = reply_tweet, in_reply_to_status_id = tweet_id)

def set_twitter_auth():
    auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api

if __name__ == "__main__": 
    api = set_twitter_auth()
    daysStreamListener = DaysStreamListener(api)
    daysStream = ty.Stream(auth = api.auth, listener=daysStreamListener)
    daysStream.filter(track=['@toughlovebot'])