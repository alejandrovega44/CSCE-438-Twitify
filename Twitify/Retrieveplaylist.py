#!/usr/bin/env python

import sys
import json
import cgi
import json,ast #or cjson
import pickle


fs = cgi.FieldStorage()

print "Content-Type: application/json"

print "\n"
print "\n"


'''def readfile():
    s = pickle.load( open( "pID.p", "rb" ) )
    for k, v in s.items():
        print s[k]'''
    
def returnID(): 
    result = {}
    availableIDs = [] 
    fetchedID = fs.getvalue("name")
    
    #f = open('IDs.txt','r')
    playlistIDs = pickle.load( open( "pID.p", "rb" ) )
    #playlistIDs = ast.literal_eval(playlistIDs)
    retID = "" 
    for k,v in playlistIDs.items():
        if k == fetchedID:
            retID = playlistIDs[k]
            break
        else:
            retID = "NOT FOUND"
    for k,v in playlistIDs.items():
        availableIDs.append(k); 
    print json.dumps([retID, availableIDs],indent=1)
    print "\n"
    sys.stdout.close()
    
def main():
    returnID()
    #readfile()
	
if __name__ == "__main__":
    main()