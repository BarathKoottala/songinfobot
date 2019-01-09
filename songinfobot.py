#Song Information Reddit Bot

import praw
import lyricsgenius as genius

#reddit api login
#app developed under the projectpersonal reddit account

reddit = praw.Reddit(client_id="Y4qCULosW04Ozw", client_secret ="kssQaeqJJNiP7oXlf9nkfTTqbEs", username="songinfobot", password="Ragi1226!", user_agent="songinfobot")
					
#subreddits that bot interacts with
subreddit = reddit.subreddit("drizzy")

#phrase to call songinfobot
keyphrase = "!songinfobot"
		

def getSongInfo(song_title):
	api = genius.Genius("4WNXyCz9LKmUBaGCkvMA0DTTbLQABKi1r6SamIY8TJubG9Q_v3ZgctwHO9i98-Hs")
	artist_name =  "Drake"
	song_response = api.search_song(song_title, artist_name)
	if song_response:
		song_information = song_response.title + " by " + song_response.artist + ".\nAppears on the album: " + song_response.album + ".\nReleased on: " + song_response.year + ". \nFind out more at: " + song_response._url
		return song_information
	else:
		print("Couldn't find " + song_name + "by " + artist_name)
		

def postToReddit():
	for comment in subreddit.stream.comments():
		if(keyphrase in comment.body):
			#Found a comment calling songinfobot so can proceed to look up song
			song_title = comment.body.replace(keyphrase, " ")
			song_info = getSongInfo(song_title)
			comment.reply(song_info)
			print("Posted: ")
			print(song_info + " to r/Drizzy")
				
				
					
postToReddit()
print("Done posting to Reddit")