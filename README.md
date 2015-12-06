#Music

####by Ben Lawson
==================

The goal of this project is to create an easier way to manipultate music and query it. This language is built from using user-submitted data to allmusic.com. In the general, the expressions relate to lyrics. I hope to all a 'play' statement that will search for the song on YouTube or similar and play from that.

Some sample queries I imagine:

Print ( Lyrics ( 'Hello' ) ) --this will be print the lyrics to a song titled 'Hello'

Print ( Lyrics (Both ( Artist ('Adele') ('Hello')))) -- this will print the lyrics to Adele's "Hello"



 
Expresions:
+ Length (song)
+ Lyrics (song)
+ Interval (song start end)
+ Style (song | artist) 
+ Artist (song) 
+ Element (word song) 
+ [ word ]
+ Both (Artist (song) (song)

Statements:
+ Print (expression)
+ Play  (expression)

