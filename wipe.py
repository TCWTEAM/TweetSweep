import csv
import json
import os.path
import time

import tweepy

with open("config.json", "r") as f:
    configObj = json.load(f)

api_key = configObj['api_key']
api_secret = configObj['api_secret']
access_token = configObj['access_token']
access_token_secret = configObj['access_token_secret']
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweetArr = []


def delete_tweets():
    total = len(tweetArr)
    print("DO NOT CLOSE THIS BEFORE COMPLETE")

    while len(tweetArr) != 0:
        tweet_id = tweetArr[0]
        tweetArr.remove(tweet_id)
        time.sleep(2)

        try:
            api.destroy_status(tweet_id)
            print("TWEET DELETED {} REMAINING {}".format(str(len(tweetArr)), tweet_id))
            print("")

        except Exception as e:
            print("ERROR TWEET {} NOT FOUND | {}".format(tweet_id, e))

    api.update_status(
        'TweetSweep Just Deleted {} Tweets From My Account. https://github.com/TCWTEAM/TweetSweep'.format(total))
    print("COMPLETE")


if __name__ == '__main__':
    print("-" * 40)
    print("TweetSweep By @ehxohd")
    print("https://github.com/tcwteam/tweetsweep")
    print("-" * 40)
    print("")

    useArchive = input("Use Archive? (Bypass 3,200 Limit) [y/n]: ")
    twitter_name = input("Twitter Username: ")

    if useArchive.lower() == "y":
        if not os.path.isfile('tweets.csv'):
            print("ERROR - NO ARCHIVE FOUND")
            exit()

        with open('tweets.csv') as csvfile:
            ader = csv.reader(csvfile)
            for row in ader:
                tweetArr.append(row[0])
    else:
        exit()

    tweets = api.user_timeline(screen_name=twitter_name)
    for tweet in tweets:
        tweetArr.append(tweet.id)

    print("Loaded {} Tweets... Initiating".format(str(len(tweetArr))))

    confirm = input("Do you really want to delete your tweets? [y/n]")

    if confirm.lower() == "y":
        delete_tweets()
    else:
        exit()
