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
# ID is the unique twitter ID for this bot's account. Might have to use later.
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


def getRandomSearchResult(api, search):
    """
    gets 100 search results of the string, search, and returns a randomly
    chosen tweet
    """
    searchResults = [status for status in ty.
                     Cursor(api.search, q=search).items(100)]
    randomTweet = searchResults[random.randint(0, len(searchResults) - 1)]
    return randomTweet


def tweetAtFollower(api):
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


def tweetAtGabby(api):
    """
    this method tweets Gabby 
    """
    message = followerReplies[random.randint(0, len(followerReplies) - 1)]
    tweet = ".@{} " + message
    gabbysHandle = 'frescopaintings'
    # check for duplicate, tweet away!
    deleteOldTweets(api, tweet.format(gabbysHandle))
    api.update_status(tweet.format(gabbysHandle))
    
def tweetAtSpook(api): 
    """
    this method tweets Spook Boy 
    """
    message = followerReplies[random.randint(0, len(followerReplies) - 1)]
    tweet = ".@{} " + message
    spookhandle = 'spookinhell'
    # check for duplicate, tweet away!
    deleteOldTweets(api, tweet.format(spookhandle))
    api.update_status(tweet.format(spookhandle))


def replyRandomTweet(api):
    """
    randomly selects a type of reply tweet and tweets to a random tweet of that
    type based on search results
    """
    randInt = random.randint(0, 2)
    if randInt == 0:
        message = worriedReplies[random.randint(0, len(worriedReplies) - 1)]
        tweet = "@{} " + message
        search = "\"I'm sad\""
        randomTweet = getRandomSearchResult(api, search)
        userHandle = randomTweet.user.screen_name
        tweetID = randomTweet.id
        deleteOldTweets(api, tweet.format(userHandle))
        api.update_status(tweet.format(userHandle), tweetID)
    elif randInt == 1:
        message = lonelyReplies[random.randint(0, len(lonelyReplies) - 1)]
        tweet = "@{} " + message
        search = "\"I'm lonely\""
        randomTweet = getRandomSearchResult(api, search)
        userHandle = randomTweet.user.screen_name
        tweetID = randomTweet.id
        deleteOldTweets(api, tweet.format(userHandle))
        api.update_status(tweet.format(userHandle), tweetID)
    elif randInt == 2:
        message = sickReplies[random.randint(0, len(lonelyReplies) - 1)]
        tweet = "@{} " + message
        search = "\"I'm sick\""
        randomTweet = getRandomSearchResult(api, search)
        userHandle = randomTweet.user.screen_name
        tweetID = randomTweet.id
        deleteOldTweets(api, tweet.format(userHandle))
        api.update_status(tweet.format(userHandle), tweetID)


def sendTweet(api):
    """
    selects a psuedo-random tweet from the tweets list, checks for duplicates,
    and tweets the message.
    """
    tweet = statusTweets[random.randint(0, len(statusTweets) - 1)]
    deleteOldTweets(api, tweet)
    api.update_status(tweet)


# main driver, chooses type of tweet to make based on time of day
if __name__ == "__main__":
    # get today's day, time (day may be used for deletion purposes later)
    time = arrow.now("US/Central").format("D HH:mm")
    # set auth token
    api = setTwitterAuth()
    # get the bot's user object
    bot = api.me()
    if time[-5::] == "11:15" or time[-5::] == "16:15":
        tweetAtFollower(api)
    elif time[-2::] == "00":
        sendTweet(api)
    elif time[-2::] == "30":
        replyRandomTweet(api)
    # THAT'S ALL, FOLKS!
    
    #separate if for Gabby and Gabby only
    if time[-5::] == "08:00" or time[-5::] == "22:00":
        tweetAtGabby(api)
        
    if time[-5::] == "08:00" or time[-5::] == "22:00":
        tweetAtSpook(api)
