#!/usr/bin/env python

#http://utkk21448ab2.tamutwitify.koding.io/Twitify/

import sys
import json
import cgi
import json,ast #or cjson
import pickle


print "Content-Type: application/json"

def GenPlaylist():
    availablePlaylists = [] 
    playlistIDs = pickle.load( open( "pID.p", "rb" ) )
    for k,v in playlistIDs.items():
        availablePlaylists.append(k)
    print 
    print json.dumps(availablePlaylists)
    return availablePlaylists
    
def main():
    GenPlaylist()
	
if __name__ == "__main__":
    main()
    
