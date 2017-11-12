#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import tweepy
import numpy as np
from nltk.tokenize import word_tokenize
from html.parser import HTMLParser
import re
import itertools
import pickle

consumer_key = "nf433d0e3PlINivICrUO1g343"
consumer_secret = "0mu0TcXWtci9N675AjDEvNNUpbG0OPNJJsM3HGRQUsUiTRNWer"
access_key = "777908743812055040-NJ5SqRaZDAbFkxsX2ZCFi8UAHBxDzEz"
access_secret = "uMjy2dMK9QT3xEC2ccMxGNiIuol1n2heg61OgiO2KWhfM"


def get_tweets(username):

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username)
        tmp=[]
        appostophes= {"’s" : " is", "’re": " are", "n’t" : " not", "’d" : " had" , "’m":" am", "’ve":" have"}
        html_parser= HTMLParser()
        #create array of tweet information: username, tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets]
        for j in tweets_for_csv:
                i=j
                i=html_parser.unescape(i)
                slist=i.split()
                newsen=[]

                for word in slist:
                    for candid in appostophes:
                        if candid in word:
                            word=word.replace(candid,appostophes[candid])
                    newsen.append(word)

                rfrm=" ".join(newsen)
                
                ans=""

                for a in re.findall('[A-Z][^A-Z]*',i):
                        ans+=a.strip()+' '
                i=ans
                ans=''.join(''.join(s)[:2] for _, s in itertools.groupby(i))
                i=ans
                i= re.sub(r"http\S+", "",i)
                
                tmp.append(i)
        f=open('tweets','wb')
        pickle.dump(tmp,f)
        f.close()
        #tweets_for_csv = tweets_for_csv.decode("utf8").encode('ascii,’ignore’)
        #tweets_for_csv = [[unicodetoascii(tweet)] for tweet in tweets]
        
        #f2=open("{0}_tweets.csv".format(username),'w+')
        #for line in f2:
        #        f2.write(line.replace("\xe2\x80\x99","'"))

        #f2.close();

if __name__ == '__main__':
        get_tweets(sys.argv[1])
        print(sys.argv[1])
