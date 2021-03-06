#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import tweepy
import time
import sys
import re
import json 
import os 
from random import randint

print "Content-type: application/json"

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

    def re_init(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_key, self.access_secret)
        self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())
        
    def search_query(self):
		#result is a dictionary of size two, we want the dict in results 
        query = "TAMUTwitify"
        tweetList = [] 
        tweetIDs = [] 
        N = 5
        _since_id = 0 
        
        f = open('Latest_Tweet_ID.txt','r')
        str_SinceID = f.read()
        _since_id = int(str_SinceID)
        
        results = self.api.search(q = query, count = N, lang = "en", since_id = _since_id)
		#tweet info is packaged with key: statuses, tweetInfo contains a list of tweet info
        tweetInfo = results["statuses"]
        
        if len(tweetInfo) == 0:
            results = self.api.search(q = query, count = N, lang = "en", result_type = "recent")
            tweetInfo = results["statuses"]
            
        for content in tweetInfo:
             ID = content['id']
             tweetIDs.append(ID)
    
        f = open('Latest_Tweet_ID.txt','w')
        f.write(str(tweetIDs[0])) 
        f.close()
        
		#We extract the text for each given tweet 
        for content in tweetInfo:
            tweetText = content['text']
            tweetText.encode('ascii', 'ignore')
            tweetList.append(tweetText)
        self.parseTweets(tweetList)
        
		
    def parseTweets(self, tweetList):
		#Data is taken in the following form "text...." (song name - artist)#playlistname #TAMUTwitify
		#Playlistname will always be the first hastag
		#Assumes that song name is first followed by artist 
        spotifyData = []
        for tweet in tweetList:
            found = re.search('\\((.+?)\\)', tweet)
            if found:
                songInfo = found.group(1)
                songInfo.replace('-','').split()
                parsedInfo = re.split(r'-',songInfo)				
                songName = parsedInfo[0]
                songArtist = parsedInfo[1]
                parsedHashTags = tweet.split("#")
                playlistName = parsedHashTags[1]
                info = songName + "+" + songArtist + "+" + playlistName
                spotifyData.append(info)       
		#return song name , song's Artist, Playlist's Name 
        return spotifyData
    
    def postPlaylist(self):
        print "\n"
        print "\n"
        fs = cgi.FieldStorage()
        d = {}
        for k in fs.keys():
            d[k] = fs.getvalue(k)
        
        print json.dumps(d, indent = 1)
        print "\n"
        sys.stdout.close()
        
def main():

    tc = TwitterCrawler()
    tc.search_query()
    tc.postPlaylist()
	
if __name__ == "__main__":
    main()