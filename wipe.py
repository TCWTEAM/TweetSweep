import csv
import json
import os.path
import tweepy
import time
import random
import json

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

def deleteTweets():
    totalt = str(len(tweetArr))
    print("DO NOT CLOSE THIS BEFORE COMPLETE")
    while len(tweetArr) != 0:
        tweetid = tweetArr[0]
        tweetArr.remove(tweetid)
        time.sleep(2)
        try:
            api.destroy_status(tweetid)
            print("TWEET DELETED {} REMAINING {}".format(str(len(tweetArr)), tweetid))
            print("")

        except Exception as e:
            print("ERROR TWEET {} NOT FOUND | {}".format(tweetid, e))
    api.update_status('TweetSweep Just Deleted {} Tweets From My Account. https://github.com/TCWTEAM/TweetSweep'.format(totalt))
    print("COMPLETE")




if __name__ == '__main__':
    print("-" * 40)
    print("TweetSweep By @ehxohd")
    print("https://github.com/tcwteam/tweetsweep")
    print("-" * 40)
    print("")
    useArchive = input("Use Archive? (Bypass 3,200 Limit) [y/n]: ")
    tname = input("Twitter Username: ")
    if useArchive.lower() == "y":
        if os.path.isfile('tweets.csv') == False:
            print("ERROR - NO ARCHIVE FOUND")
            exit()

        with open('tweets.csv') as csvfile:
            ader = csv.reader(csvfile)
            for row in ader:
                tweetArr.append(row[0])

    tweets = api.user_timeline(screen_name=tname)
    for tweet in tweets:
        tweetArr.append(tweet.id)
    print("Loaded {} Tweets... Initiating".format(str(len(tweetArr))))
    confirm = input("If You Really Want To Delete Your Tweets Type 'ehxohd': ")
    if confirm == "ehxohd":

        deleteTweets()
    else:
        exit()
