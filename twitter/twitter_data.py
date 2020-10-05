import tweepy
from textblob import TextBlob
from twitter.twitter_auth import *
from twitter.twitter_util import clean, pie

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# ambil data dari timeline salah satu akun
liverpool = api.user_timeline(id="LFC", count="5", tweet_mode="extended")

# ambil data berdasarkan kata kunci
keyword = "wfh"
resultSearch = api.search(q=[keyword], lang="id", count="10", tweet_mode="extended")

positive_tweets = 0
neutral_tweets = 0
negative_tweets = 0
for tweet in resultSearch:
    tweet_clean = clean(tweet.full_text)
    analysis = TextBlob(tweet_clean)
    try:
        analysis = analysis.translate(to="en", from_lang="id")
    except Exception as e:
        print(e)
    polarity = analysis.polarity
    if polarity > 0.0:
        positive_tweets += 1
    elif polarity == 0.0:
        neutral_tweets += 1
    else:
        negative_tweets += 1

total = positive_tweets + neutral_tweets + negative_tweets
print("Positive: {:.2f}%".format(100 * positive_tweets / total))
print("Neutral: {:.2f}%".format(100 * neutral_tweets / total))
print("Negative: {:.2f}%".format(100 * negative_tweets / total))
labels = ["Positive", "Neutral", "Negative"]
values = [positive_tweets, neutral_tweets, negative_tweets]
title = "keyword: " + keyword
pie(labels, values, title)
