import sys
import spotipy
import spotipy.util as util
import pprint

#export SPOTIPY_CLIENT_SECRET='d84b72337f77420baed1f106fa8de225'
#export SPOTIPY_CLIENT_ID='c2c2bcc1b5444f90ae9a63968129d160'

#scope = 'user-library-read'
scope = 'playlist-modify-public'
username = 'TamuTwitify'

artist_name = "Chop Suey"
song_name = "System of a Down"
_id = []  #track IDs
playlist_id =''
token = util.prompt_for_user_token(username, scope)
sp

def check_playlist(name): 
	#if playlist is in file, set playlist  ID
	#else make playlist and set  playlist ID
	
	sp.user_playlist_create(username, name, public=True)
	playlists = sp.user_playlists(username)
	for playlist in playlists['items']:
		print playlist['name']
		if playlist['name'] == name:
			print 'found playlist' + playlist['id']
			playlist_id =  playlist['id']

	
def add_song_to_playlist(title, artist, playlist_name):
	
	#seach for all of artists songs
	r = sp.search(q="artist:" + artist, limit=50)
	#find the song from the list of songs returned
	for i, t in enumerate(r['tracks']['items']):
		if t['name'] == title:
			print t['id']
			_id.append(t['id'])
			break;
	#add song to playlist		
	result = sp.user_playlist_add_tracks(username, playlist_id, _id)
	print result


def main():
	if token:
	    sp = spotipy.Spotify(auth=token)
	    add_song_to_playlist(song_name, artist_name, 'WTF')
	else:
		print "Can't get token for", username

	
if __name__ == "__main__":
    main()
