# testing
import datetime
from collections import Counter

import random
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from collections import Counter
import tweepy
import twint
from graphics import *


def textblob_adj(text):
    blobed = TextBlob(text)
    counts = Counter(tag for word, tag in blobed.tags)
    adj_list = []
    adv_list = []
    adj_tag_list = ['JJ', 'JJR', 'JJS']
    adv_tag_list = ['RB', 'RBR', 'RBS']
    for (a, b) in blobed.tags:
        if b in adj_tag_list:
            adj_list.append(a)
        elif b in adv_tag_list:
            adv_list.append(a)
        else:
            pass
    return adj_list, adv_list, counts['JJ'] + counts['JJR'] + counts['JJS'], counts['RB'] + counts['RBR'] + counts[
        'RBS']


def sentiment():
    test_subset = ['20170412', 'great', 'bad', 'terrible', 'dog', 'stop', 'good']

    sid = SentimentIntensityAnalyzer()
    pos_word_list = []
    neu_word_list = []
    neg_word_list = []

    for word in test_subset:
        if (sid.polarity_scores(word)['compound']) >= 0.5:
            pos_word_list.append(word)
        elif (sid.polarity_scores(word)['compound']) <= -0.5:
            neg_word_list.append(word)
        else:
            neu_word_list.append(word)

    print('Positive :', pos_word_list)
    print('Neutral :', neu_word_list)
    print('Negative :', neg_word_list)


def word_polarity(text):
    words = text.split(' ')
    pos_word_list = []
    neu_word_list = []
    neg_word_list = []

    for word in words:
        testimonial = TextBlob(word)
        if testimonial.sentiment.polarity >= 0.5:
            pos_word_list.append(word)
        elif testimonial.sentiment.polarity <= -0.5:
            neg_word_list.append(word)
        else:
            neu_word_list.append(word)

    print('Positive :', pos_word_list)
    print('Neutral :', neu_word_list)
    print('Negative :', neg_word_list)


def sentence_polarity(text):
    testimonial = TextBlob(text)
    return testimonial.sentiment.polarity, testimonial.sentiment.subjectivity


def search_tweets():
    key = "HKJF3rdUcTflkEhSstSIaJEtK"
    secret = "TUUUqOwVZWIYiRENmKJzJpIqDV4CNMtYRpiei5CjbgRGeHPUfM"
    auth = tweepy.AppAuthHandler(key, secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    # api.update_status("Look, I'm tweeting from #Python.")

    tweets = []
    for tweet in tweepy.Cursor(api.search,
                       q="google",
                       rpp=100,
                       result_type="recent",
                       include_entities=True,
                       lang="en").items():
        tweets.append(tweet)

    return tweets


def get_tweets(user):
    key = "HKJF3rdUcTflkEhSstSIaJEtK"
    secret = "TUUUqOwVZWIYiRENmKJzJpIqDV4CNMtYRpiei5CjbgRGeHPUfM"
    auth = tweepy.AppAuthHandler(key, secret)
    api = tweepy.API(auth)
    #api.update_status("Look, I'm tweeting from #Python.")
    api = tweepy.API(auth)

    tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, id=user).items(100):
        if tweet.lang == 'en':
            tweets.append(tweet)

    return tweets


def get_tweets_date(user, since, until):
    key = "HKJF3rdUcTflkEhSstSIaJEtK"
    secret = "TUUUqOwVZWIYiRENmKJzJpIqDV4CNMtYRpiei5CjbgRGeHPUfM"
    auth = tweepy.AppAuthHandler(key, secret)
    api = tweepy.API(auth)
    #api.update_status("Look, I'm tweeting from #Python.")
    api = tweepy.API(auth)
    page = 1
    stop_loop = False
    while not stop_loop:
        print('.' + str(page) + '.')
        tweets = api.user_timeline(user, page=page)
        if not tweets:
            break
        for tweet in tweets:
            if since < tweet.created_at < until and text.lang == 'en':
                print("%-160s   %s" % (tweet.text, tweet.created_at))
                stop_loop = True
                break
            # Do the tweet process here

        page += 1
        time.sleep(500)


def twint_get():
    # Configure
    config = twint.Config()
    config.Username = "realDonaldTrump"
    config.Since = "2020-01-01"
    config.Until = "2020-01-31"
    config.Store_json = True
    config.Output = "custom_out.json"
    # Run
    twint.run.Search(config)


def draw(user, color, win):
    i = 0
    start = datetime.datetime(2020, 6, 1, 0, 0, 0)
    end = datetime.datetime(2020, 6, 2, 0, 0, 0)
    for text in get_tweets(user):
        sentiment = sentence_polarity(text)
        print("%-160s   %s" % (text, sentiment))
        y = sentiment[0]
        n = Circle(Point(i * 1, y * 50 + 50), .5)
        n.setWidth(0)
        n.setFill(color)
        n.draw(win)
        i += 1

def main2():
    win_w = 900
    win_h = 900
    win = GraphWin("frog", win_w, win_h)  # make a graphics window
    win.setBackground(color_rgb(150, 150, 150))
    win.setCoords(0, 0, 100, 100)
    l = Line(Point(0, 50), Point(100, 50))
    l.setWidth(1)
    l.setFill(color_rgb(80, 80, 80))
    l.draw(win)

    #draw("JustinTrudeau", color_rgb(10, 10, 10), win)
    draw("RealDonaldTrump", color_rgb(100, 10, 10), win)
    win.getMouse()


def main():
    ts = get_tweets("RealDonaldTrump")
    for t in ts:
        sentiment = sentence_polarity(t.text)
        print("%-25s %-10.2f %-10.2f" % (str(t.created_at), sentiment[0], sentiment[1]))


if __name__ == "__main__":
    main()

