import tweepy as tw
import pandas as pd
import os
import csv

API_KEY = "IQFN7RfvSs3107ZGKq1vDE2Um"
API_KEY_SECRET = "JF8rB1ftzNPzNKCUGHTZXtZV22yiCK51bJnl51t1riNnLy4cuJ"
consumer_key = "IQFN7RfvSs3107ZGKq1vDE2Um"
consumer_secret = "JF8rB1ftzNPzNKCUGHTZXtZV22yiCK51bJnl51t1riNnLy4cuJ"
access_token = "1008966897130303488-PNJTNYKhrs5q3YbCIZf2lRGC817JSQ"
access_token_secret = "89xKwZBAZBUHLVqoayE1gDGfuJeJwzLhnkZ7NnXvOJZ6v"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

tweets_df = pd.read_csv("tweet_ids.csv")

twitter_ids = tweets_df["tweet_id"].tolist()
ids = twitter_ids[1:10]
tweets = []
for tweet_id in ids:
    print("Processing tweet. ID = " + tweet_id)
    tweet = api.get_status(tweet_id)
    tweets.append(tweet.text)
    print(tweet.text)

print("writing to dataset")
with open("tweets.txt", "w") as f:
    for tweet in tweets:
        print("writing to txt file. tweet: " + str(tweet))
        f.write("%s\n" % str(tweet))
