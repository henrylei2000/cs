# testing
import datetime
from collections import Counter

import random
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from collections import Counter

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
    return adj_list, adv_list, counts['JJ']+counts['JJR']+counts['JJS'], counts['RB']+counts['RBR']+counts['RBS']


def sentiment():
    test_subset=['20170412', 'great', 'bad', 'terrible', 'dog', 'stop', 'good']

    sid = SentimentIntensityAnalyzer()
    pos_word_list=[]
    neu_word_list=[]
    neg_word_list=[]

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


def word_polarity(test_subset):
    pos_word_list=[]
    neu_word_list=[]
    neg_word_list=[]

    for word in test_subset:
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
    print(format(testimonial.sentiment))


def main():
    text = "I hate Monday but I love California"
    sentence_polarity(text)
    print(textblob_adj(text))
    # sentiment()
    word_polarity(['20170412', 'great', 'bad', 'terrible', 'dog', 'stop', 'good'])
    blob3 = TextBlob("I hate Monday but I love California")
    print(format(blob3.sentiment))


main()