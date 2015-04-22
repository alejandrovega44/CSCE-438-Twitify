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

import spotipy
import spotipy.util as util

#print "Content-type: application/json"

username = 'TamuTwitify'
_id = []  #track IDs
playlist_id =''
scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)
sp = spotipy.Spotify(auth=token)

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
        
    def check_playlist(self, name): 
		try:
			#try to find existing playlist 
			playlists = sp.user_playlists('tamutwitify')
			for playlist in playlists['items']:
				if playlist['name'].lower() == name.lower():
					return playlist['id']
			# if can't find make a new one	
			print "Creating playlist"		
			sp.user_playlist_create('tamutwitify', name, public=True)
			playlists = sp.user_playlists('tamutwitify')
			for playlist in playlists['items']:
				if playlist['name'].lower() == name.lower():
					return playlist['id']
		except spotipy.SpotifyException:
			print "could not create playlist"

    def add_song_to_playlist(self, title, artist, playlist_name):
    	print "finding song" , title, artist, playlist_name
    	#seach for all of artists songs
    	r = sp.search(q= str(artist) + " " +str(title), limit=50)
    	#find the song from the list of songs returned
    	for i, t in enumerate(r['tracks']['items']):
    		print t['name'] +" " + t['id'] 
    		_id.append(t['id'])
    		break;
		pList_id = self.check_playlist(str(playlist_name))
		#add song to playlist
		
		try:
			result = sp.user_playlist_add_tracks('tamutwitify', str(pList_id), _id)
			return 0
		except spotipy.SpotifyException:
			print "could not add song"
			return 1
			
    def search_query(self):
		#result is a dictionary of size two, we want the dict in results 
        query = "TAMUTwitify"
        tweetList = [] 
        tweetIDs = [] 
        N = 2
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
                print songName, songArtist, playlistName
                self.add_song_to_playlist(songName, songArtist, playlistName)
		#return song name , song's Artist, Playlist's Name 
		#print spotifyData
        return spotifyData
    
    '''def postPlaylist(self):
        print "\n"
        print "\n"
        fs = cgi.FieldStorage()
        d = {}
        for k in fs.keys():
            d[k] = fs.getvalue(k)
        
        print json.dumps(d, indent = 1)
        print "\n"
        sys.stdout.close()
        '''
def main():

    tc = TwitterCrawler()
    tc.search_query()
    #tc.postPlaylist()
	
if __name__ == "__main__":
    main()
