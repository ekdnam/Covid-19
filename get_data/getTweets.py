# coding: utf-8

import tweepy as tw
import pandas as pd
import os
import csv


consumer_key = "IQFN7RfvSs3107ZGKq1vDE2Um"
consumer_secret = "JF8rB1ftzNPzNKCUGHTZXtZV22yiCK51bJnl51t1riNnLy4cuJ"
access_token = "1008966897130303488-PNJTNYKhrs5q3YbCIZf2lRGC817JSQ"
access_token_secret = "89xKwZBAZBUHLVqoayE1gDGfuJeJwzLhnkZ7NnXvOJZ6v"


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

tweets_df = pd.read_csv("tweet_ids.csv")
tweets_df.head()


index_manager_read = open("state_managers/index_manager.txt", "r")
indx = index_manager_read.read()
print(indx)
index_manager_read.close()


twitter_ids = tweets_df["tweet_id"].tolist()
i = 0
indx = int(indx)
ids = twitter_ids[indx : indx + 899]

text = []
id_str = []
entities_hashtags = []
entities_symbols = []
entities = []
user_id = []
entities_hashtags = []
entitites_symbols = []
user_location = []
time_zone = []
lang = []
created_at = []
coordinates = []

cnt = 0


# ids = twitter_ids[:10]

for tweet_id in ids:

    print("\nCurrent indx: " + str(indx))
    print("Tweets to be processed: " + str(900 - cnt))
    cnt += 1
    indx += 1

    try:
        print("Processing tweet. ID = " + str(tweet_id))

        tweet = api.get_status(tweet_id, tweet_mode="extended", include_entities=True)

        text.append(tweet.full_text)
        created_at.append(tweet.created_at)
        id_str.append(tweet.id_str)
        entities.append(tweet.entities)
        user_id.append(tweet.user.id)
        lang.append(tweet.lang)
        time_zone.append(tweet.user.time_zone)
        user_location.append(tweet.user.location)
        entities_hashtags.append(tweet.entities["hashtags"])
        entities_symbols.append(tweet.entities["symbols"])
        coordinates.append(tweet.coordinates)

        if cnt % 100 == 0:
            print("Text: " + str(tweet.full_text))
    except tw.error.TweepError:
        print("ERROR WHILE ACCESSING TWEET. ID: " + str(tweet_id))
        pass


indx_manager_write = open("state_managers/index_manager.txt", "w")
indx_manager_write.write(str(indx))
indx_manager_write.close()
print(str(indx))


text_2 = text
for ttext in text:
    ttext = ttext.strip("\n")


#         text.append(tweet.full_text)
#         created_at.append(tweet.created_at)
#         id_str.append(tweet.id_str)
#         entities.append(tweet.entities)
#         user_id.append(tweet.user.id)
#         location.append(tweet.user.location)
#         lang.append(tweet.lang)
#         time_zone.append(tweet.user.time_zone)

entities_hashtags_series = pd.Series(entities_hashtags)
entities_symbols_series = pd.Series(entities_symbols)


import pandas as pd

# df = pd.DataFrame(columns=['id_str', 'user_id', 'text', 'created_at', 'entities', 'location', 'lang', 'time_zone'])
df = pd.DataFrame(
    columns=[
        "id_str",
        "user_id",
        "text",
        "created_at",
        "lang",
        "entities_hashtags",
        "entities_symbols",
        "location",
        "coordinates",
        "time_zone",
    ]
)
df.head()

df["id_str"] = id_str
df["user_id"] = user_id
df["text"] = text
df["created_at"] = created_at
# df['entities'] = entities
df["location"] = user_location
df["lang"] = lang
df["entities_hashtags"] = entities_hashtags_series
df["entities_symbols"] = entities_symbols_series
df["lang"] = lang
df["time_zone"] = time_zone
df["coordinates"] = coordinates


print(df.head())


print("opening file manager")
file_new = open("state_managers/file_manager.txt", "r")
file_indx = file_new.read()
file_new.close()
filename = "final_tweets_" + file_indx + ".csv"
# filename = 'final_tweets_1.csv'
print("output filename is " + filename)


# filename = "final_tweets_6.csv"
print("writing df to file")
df.to_csv("dataset/" + filename)


file_indx = int(file_indx)
file_indx += 1

file_write = open("state_managers/file_manager.txt", "w")
file_write.write(str(file_indx))
file_write.close()


print("file index is " + str(file_indx))


######## DO NOT RUN #################


# print("writing to dataset")
# with open("tweets.txt", "w+") as f:
#     for tweet in tweets:
#         print("writing to txt file. tweet: " + str(tweet))
#         f.write("%s\n" % str(tweet))

# print("writing to dataset")
# with open("dates.txt", "w+") as f:
#     for date in dates:
#         print("writing to txt file. tweet: " + str(date))
#         f.write("%s\n" % str(date))


# id_t = tweets_df['tweet_id'].tolist()[1]
# tweet_2 = api.get_status(id_t, tweet_mode = 'extended')
# print(tweet_2.full_text)
