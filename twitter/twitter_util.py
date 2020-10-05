import re
import matplotlib.pyplot as plt


def clean(tweet):
    tweet_clean = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    return tweet_clean


def pie(labels, values, title):
    plt.title(title)
    explode = (0.1, 0, 0)  # explode 1st slice
    plt.pie(values, explode=explode, labels=labels,
            autopct='%0.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()
