# songinfobot
Personal project for creating a Reddit bot that post information regarding songs.

songinfobot utilizes functions from already existing libraries including Reddit's PRAW library and Genius.com's python developer library.
songinfobot currently runs on the subreddit r/Drizzy and is able to be called with the !songinfobot ***song_name*** comment.
songinfobot operates by reading through the current comment streams on the subreddit looking for the keyphrase to call, then
extracts the song name from the comment, and utilizes Genius.com's api to do a song request and obtain key information such as
the album name, release date, and url of the corresponding page on Genius.com.
