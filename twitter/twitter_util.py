import re


def clean(tweet):
    tweet_clean = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    return tweet_clean

#exercise 1
def sentimen_text(sentimen_val):
    # buat logic untuk mengubah value menjadi text
    # menggunakan conditional IF/ELSE
    # kemungkinan nilai: POSITIVE, NEUTRAL, NEGATIVE
    return ""

#exercise 2
def sentimen_percentage(tweets):
    return "positif => 30%\nnetral => 40%\nnegative => 30%"