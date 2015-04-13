import sys
import spotipy
import spotipy.util as util
import pprint

#export SPOTIPY_CLIENT_SECRET=''
#export SPOTIPY_CLIENT_ID=''
#export SPOTIPY_REDIRECT_URI=''


#scope = 'user-library-read'
scope = 'playlist-modify-public'
username = 'TamuTwitify'
artist_name = "Feel Good Inc."
song_name = "gorillaz"
_id = []  #track IDs
playlist_id =''
token = util.prompt_for_user_token(username, scope)
sp = spotipy.Spotify(auth=token)

def check_playlist(name): 
	#if playlist is in file, set playlist  ID
	#else make playlist and set  playlist ID
	
	sp.user_playlist_create(username, name, public=True)
	playlists = sp.user_playlists(username)
	for playlist in playlists['items']:
		print playlist['name']
		if playlist['name'].lower() == name.lower():
			print 'found playlist' + playlist['id']
			playlist_id =  playlist['id']

	
def add_song_to_playlist(title, artist, playlist_name):
	
	print "finding song"
	#seach for all of artists songs
#	r = sp.search(q="artist:" + artist, limit=50)
	r = sp.search(q= artist + " " +title, limit=50)
	#find the song from the list of songs returned
	for i, t in enumerate(r['tracks']['items']):
		print t['name'] +" " + t['id'] 
		#if (t['name'].lower()) == title.lower():
			#print sp.track(t['id'])
		_id.append(t['id'])
		break;
	#add song to playlist		
	#result = sp.user_playlist_add_tracks(username, playlist_id, _id)
	#print result


def main():
	
	if len(sys.argv) > 1:
		username = sys.argv[1]
		print username
	else:
		print "Usage: %s username playlist-name" % (sys.argv[0],)
		sys.exit()
    
	if token:
	    sp = spotipy.Spotify(auth=token)
	    add_song_to_playlist(song_name, artist_name, 'WTF')
	else:
		print "Can't get token for", username

	
if __name__ == "__main__":
    main()
