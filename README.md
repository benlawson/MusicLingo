#Music

####by Ben Lawson
==================

The goal of this project is to create an easier way to manipultate music and query it. This language is built from using user-submitted data to allmusic.com. In the general, the expressions relate to lyrics. I hope to all a 'play' statement that will search for the song on YouTube or similar and play from that.

Some sample queries I imagine:
```
Print ( Lyrics ( 'Hello' ) ) --this will be print the lyrics to a song titled 'Hello'
```
```
Print ( Lyrics (Both ( Artist ('Adele') ('Hello') ) ) ) -- this will print the lyrics to Adele's "Hello"
```
```
song   s :: == any title of a song
artist a :: == any music artist 
number n :: == natural numbers 
word   w :: == an English word

term   t ::==  
       s 
     | Artist (a) 
     | Both (Artist a s ) 

lyrics l  :: ==
       Lyrics (t)
   
formula f :: ==
       Length (l)
     | Interval (l n n)
     | Element (w l) 
     | Mode (l) 
     | Sentiment (l) 
     | Style (t) 

statement S :: ==
       Print (f) S
     | Play  (f) S
     | 
    
```

How To use:
The two statements, Print and Play, will either print to the screen information about the queries or play the information (audio), respectively. 

Formulas to use:
Length will return a number that represents the number of words in the song.
Interval will return the lyrics between the two number inverals

Mode returns the most common word in a song
Sentiment uses IBM BlueMix Personality Insights to determine personality keywords to describe the song.

The formulas are used to build up queries. These act upon terms, which are either a song or an artist. 

Currently need to have spaces in between each paren. 




##Setup

```
git clone https://github.com/benlawson/MusicLingo.git
cd MusicLingo
virtualenv musicenv
source musicenv/bin/activate
pip install -r requirements.txt
wget http://people.bu.edu/balawson/key.txt
```

