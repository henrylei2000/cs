# testing
import datetime
from collections import Counter

import random
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from collections import Counter
import tweepy

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
    return format(testimonial.sentiment)


def get_tweets():
    key = "HKJF3rdUcTflkEhSstSIaJEtK"
    secret = "TUUUqOwVZWIYiRENmKJzJpIqDV4CNMtYRpiei5CjbgRGeHPUfM"
    auth = tweepy.AppAuthHandler(key, secret)
    api = tweepy.API(auth)
    #api.update_status("Look, I'm tweeting from #Python.")
    api = tweepy.API(auth)

    tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, id="realDonaldTrump").items(10):
        tweets.append(tweet.text)

    return tweets


def main():
    for text in get_tweets():
        print("%-160s   %s" % (text, sentence_polarity(text)))



main()
