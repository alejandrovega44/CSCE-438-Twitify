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

	try:
		playlists = sp.user_playlists('tamutwitify')
		for playlist in playlists['items']:
			if playlist['name'].lower() == name.lower():
				return playlist['id']
				
		print "Creating playlist"		
		sp.user_playlist_create('tamutwitify', name, public=True)
		playlists = sp.user_playlists('tamutwitify')
		for playlist in playlists['items']:
			if playlist['name'].lower() == name.lower():
				return playlist['id']
		
	except spotipy.SpotifyException:
		print "could not create playlist"
		
	'''playlists = sp.user_playlists(username)
	for playlist in playlists['items']:
		print playlist['name']
		if playlist['name'].lower() == name.lower():
			print 'found playlist' + playlist['id']
			playlist_id =  playlist['id']
	'''
	
def add_song_to_playlist(title, artist, playlist_name):
	
	print "finding song"
	#seach for all of artists songs
	r = sp.search(q= artist + " " +title, limit=50)
	#find the song from the list of songs returned
	for i, t in enumerate(r['tracks']['items']):
		print t['name'] +" " + t['id'] 
		_id.append(t['id'])
		break;
	pList_id = check_playlist(playlist_name)
	#add song to playlist
	try:
		result = sp.user_playlist_add_tracks('tamutwitify', str(pList_id), _id)
	except spotipy.SpotifyException:
		print "could not add song" 
	#print result


def main():
	
	if len(sys.argv) > 1:
		username = sys.argv[1]
		print username
	else:
		print "Usage: %s playlist-name" % (sys.argv[0],)
		sys.exit()
    
	if token:
	    sp = spotipy.Spotify(auth=token)
	    song = raw_input('Enter song name: ')
	    artist = raw_input('Enter artist name: ')
	    add_song_to_playlist(song, artist, str(sys.argv[1]))
	else:
		print "Can't get token for", username

	
if __name__ == "__main__":
    main()
