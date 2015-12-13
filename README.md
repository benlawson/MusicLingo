#Music

####by Ben Lawson
==================

The goal of this project is to create an easier way to manipultate music and query it. This language is built from using user-submitted data to allmusic.com. In the general, the expressions relate to lyrics. I hope to all a 'play' statement that will search for the song on YouTube or similar and play from that.

Some sample queries I imagine:
```
Print ( Lyrics ( 'Hello' ) ) --this will be print the lyrics to a song titled 'Hello'
```
```
Print ( Lyrics (Both ( Artist ('Adele') ('Hello')))) -- this will print the lyrics to Adele's "Hello"
```
song s :: == any title of a song
artist a :: == any music artist 
number n :: == natural numbers 

term t ::==  
    + s 
    + | Artist (s) 
    + | [ t ]


formula f :: ==
    + Length (s)
    + | Lyrics (s)
    + | Interval (s n n)
    + | Style (t) 
    + | Element (w s) 
    + | Both (Artist (song) (song)) 

Statements:
+ Print (f)
+ Play  (f)

