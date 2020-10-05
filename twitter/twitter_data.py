import tweepy
from textblob import TextBlob
from twitter.twitter_auth import *
from twitter.twitter_util import clean

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# ambil data dari timeline salah satu akun
liverpool = api.user_timeline(id="LFC", count="5")

# ambil data berdasarkan kata kunci
resultSearch = api.search(q=["wfh"], lang="id", count="10", tweet_mode="extended")

print("========= tweet with keyword: covid =======")
tweets = []
for tweet in resultSearch:
    # print(tweet)
    tweet_clean = clean(tweet.full_text)
    analysis = TextBlob(tweet_clean)
    try:
        analysis.translate(to="en")
    except Exception as e:
        print(e)
    tweet_dict = {"text": tweet_clean, "polarity": analysis.polarity}
    tweets.append(tweet_dict)
    print("ori      => ", tweet.full_text)
    print("clean    => ", tweet_clean)
    print("sentimen => ", analysis.polarity)
    print("======================")

print("========== FINAL ============")
print(tweets)
