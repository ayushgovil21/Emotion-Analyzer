#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import tweepy
import numpy as np
from nltk.tokenize import word_tokenize

consumer_key = "nf433d0e3PlINivICrUO1g343"
consumer_secret = "0mu0TcXWtci9N675AjDEvNNUpbG0OPNJJsM3HGRQUsUiTRNWer"
access_key = "777908743812055040-NJ5SqRaZDAbFkxsX2ZCFi8UAHBxDzEz"
access_secret = "uMjy2dMK9QT3xEC2ccMxGNiIuol1n2heg61OgiO2KWhfM"


def get_tweets(username):

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        number_of_tweets=200
        tweets = api.user_timeline()

        #create array of tweet information: username, tweet id, date/time, text
        tweets_for_csv = [[tweet.text.encode('ascii','ignore')] for tweet in tweets]
        #tweets_for_csv = tweets_for_csv.decode("utf8").encode('ascii,’ignore’)
        #tweets_for_csv = [[unicodetoascii(tweet)] for tweet in tweets]

        with open("{0}_tweets.csv".format(username) , 'w+') as file:
                writer = csv.writer(file)
                writer.writerows(tweets_for_csv)

        #f2=open("{0}_tweets.csv".format(username),'w+')
        #for line in f2:
        #        f2.write(line.replace("\xe2\x80\x99","'"))

        #f2.close();

if __name__ == '__main__':

     get_tweets("BDUTT")
     f=open('BDUTT.csv','r')
     #for line in f:
             #words[3]=word_tokenize(line)
             
    #   get_tweets(sys.argv[1])


     #f=open('ayush_govil_tweets.csv','r')
     #count=0
     #for line in f:
      #   for word in line.split('|'):
       #      count=count+1
        #     if(count==4):
         #        for phrases in word.split(" "):
          #           print(phrases)
           #      print("\n")
         #count=0

     #f.close()
