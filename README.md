#Music

####by Ben Lawson
==================

The goal of this project is to create an easier way to manipultate music and query it. This language is built from using user-submitted data to allmusic.com. In the general, the expressions relate to lyrics. I hope to all a 'play' statement that will search for the song on YouTube or similar and play from that.

Some sample queries:
```
interact('')
```
Print a the most common word of a random song by Adele
```
>'print ( mode ( lyrics ( adele ) ) ) ' 
['had']

```
Print the most common word in the song 'Hello' by Adele
```
>'print ( mode ( lyrics ( both ( artist ( adele hello ) ) ) ) )'
['you']
```

Print the lengh of the song Hotline Bling
```
>'print ( length ( lyrics ( hotline bling ) ) ) '
[373]
```

Print the 'personality' of the song Hello by Adele
```
>'print ( sentiment ( lyrics ( both ( artist ( adele hello ) ) ) ) )'
[[u'Orderliness', u'Assertiveness', u'Excitement-seeking', u'Gregariousness']]
```

```
*number n* :: == natural numbers 
*word   w* :: == an English word, song, or artist

*term t* :: ==
       left 
     | left **and** t

*left* :: ==
       **Song** w
     | **Artist** w
     
*lyrics l*  :: ==
      **Lyrics** (t) 
   
*formula f* :: ==
       **Length** (l)
     | **Interval** (l n n)
     | **Element** (w l) 
     | **Mode** (l) 
     | **Sentiment** (l) 
     | **Style** (t) 

*statement S* :: ==
       **Print** (f) S ; 
     | **Play**  (f) S ;
     |  
    
```

How To use:
The two statements, Print and Play, will either print to the screen information about the queries or play the information (audio), respectively. 

Formulas to use:
+ Length will return a number that represents the number of words in the song.
+ Interval will return the lyrics between the two number inverals
+ Mode returns the most common word in a song
+ Sentiment uses IBM BlueMix Personality Insights to determine personality keywords to describe the song.

Currently need to have spaces in between each paren. 



##Setup

```
git clone https://github.com/benlawson/MusicLingo.git
cd MusicLingo
virtualenv musicenv
source musicenv/bin/activate
pip install -r requirements.txt
wget http://people.bu.edu/balawson/key.txt #for IBM BlueMix credentials
```

