# CSCE-438-Twitify

Twitify is a Web Application that integrates the functionalities of Twitter and Spotify.
Twitify will allow users to send Tweets to #TAMUTwitify containing (song name - artist) #PlaylistName #TAMUTwitify which will create a Playlist for that user containing the spefied song. 


In order to run this code, Koding.com was used. The following steps are specific to using Koding.com.

Steps:

1) From the Koding terminal enter the following line: 
		sudo -H  pip install requests==2.5.3 (this downloads an older version of ubuntu) 

2) Change the current directory to Web and download packages tweepy.py and spotipy.py. From the terminal enter: 
				sudo -H pip install tweepy.py 
   
   and the same with spotipy.py (If you have not downloaded pip use the following line: sudo apt-get install python-pip)
   
3) In the Web directory download the code from git with the following line: 

		sudo git clone https://github.com/alejandrovega44/CSCE-438-Twitify

4) In the far left of your koding session, click on koding-vm-x and click on you assinged urls. Enter the following url:
			
		http://"Your Assigned Url"/CSCE-438-Twitify/Twitify/

5) Play around with it