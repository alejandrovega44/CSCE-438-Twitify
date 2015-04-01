#!/usr/bin/env python
# -*- coding: utf-8  -*-
#encoding=utf-8

# ********************************************PLEASE READ*************************************************************** 
# Twitter search limit is 180 tweets per 15 min interval. Max number of tweets we can retrieve per request is 100 
# Used spaces to format code 
# In order to run this code, you will need to download the Tweepy package

#***********************************************************************************************************************

import tweepy
import time
import sys
import re
import cgi, cgitb 
import json 
import os 
from random import randint

class TwitterCrawler():
    #Add twitter auth tokens
    consumer_key = ""
    consumer_secret = ""
    access_key = ""
    access_secret = ""
    auth = None
    api = None

    def __init__(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_key, self.access_secret)
        self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())
        #print self.api.rate_limit_status()

    def re_init(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_key, self.access_secret)
        self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())

    def search_query(self):
		#result is a dictionary of size two, we want the dict in results 
        query = "TAMUTwitify"
        tweetList = [] 
        N = 5
        #_since_id = retrive latest tweet 
		#remove result_type since we will use since_id 
		#each time this code is ran, we need to save the ID of the most recent tweet, and begin our next retrieval with this ID as the starting point 
        results = self.api.search(q = query, count = N, lang = "en", result_type = "recent" """since_id = _since_id""")
		#tweet info is packaged with key: statuses, tweetInfo contains a list of tweet info
        tweetInfo = results["statuses"] 
		#We extract the text for each given tweet 
        for content in tweetInfo:
            tweetText = content['text']
            tweetText.encode('ascii', 'ignore')
            tweetList.append(tweetText)
        print tweetList
	
	#tokenizes extracted tweets 	
    def tokenize(self, tweetList):
        tokenList = []
		#tokenizing tweets for the each query 
        for tweets in query_tweets:
            tweet = tweets.lower()
            tokens = re.findall(r"[\w']+",tweet)
            for words in tokens:
				tokenList.append(words)
        return tokenList

def main():

    tc = TwitterCrawler()
    tc.search_query()
	
if __name__ == "__main__":
    main()