#Music

####by Ben Lawson
==================

The goal of this project is to create an easier way to manipultate music and query it. This language is built from using user-submitted data to allmusic.com. In the general, the expressions relate to lyrics. I hope to all a 'play' statement that will search for the song on YouTube or similar and play from that.

Some sample queries:
```
python interpret.py
```
Print a the most common word of a random song by Adele
```
> print mode ( lyrics ( song adele ) ) ;
['had']

```
Print the most common word in the song 'Hello' by Adele
```
> print mode ( lyrics ( artist adele and song hello ) ) ;
['you']
```

Print the lengh of the song Hotline Bling
```
> print length ( lyrics ( song hotline bling ) ) ;
[373]
```

Print the 'personality' of the song Hello by Adele
```
>print sentiment ( lyrics ( artist adele and song hello ) ) ;
[[u'Orderliness', u'Assertiveness', u'Excitement-seeking', u'Gregariousness']]
```
Check if a word is in the lyrics
```
>print element ( hate lyrics ( artist taylor swift and song love ) ) ;
[True]
```

Check the moods of an artist or song
```
>print moods ( artist taylor swift ) ;
 ['Cathartic Earnest Passionate Sentimental Warm Exuberant Reflective Sophisticated Carefree Confident Gentle Laid-Back/Mellow Organic Playful Refined Springlike Sweet Yearning Amiable/Good-Natured Bittersweet Cheerful Confrontational Theatrical Angst-Ridden Relaxed Romantic Clinical Effervescent Poignant']
```
Check the styles of an artist or song
```
>print styles ( artist taylor swift and song love story) ;
['Contemporary_Country Country-Pop Pop']
```

Check the genre of an artist or song
```
>print genre ( artist taylor swift and song love story) ;
['Country Pop/Rock']
```


Play statement: works on Mac or Linux with *gnustep-gui-runtime* package installed
on Debian-based systems you install via:
```
sudo apt-get install gnustep-gui-runtime
```

```
>play lyrics (artist adele and song hello ) ;
['you should hear this']
```

Play just the first 100 words of song: 
```
>play interval ( lyrics ( artist taylor swift and song love ) 0 100 ) ;
['you should hear this']
```


```
number n :: == natural numbers 
word   w :: == an English word, song, or artist

term t :: ==
     left 
   | left and t

left :: ==
     Song w
   | Artist w
     
lyrics l  :: ==
    Lyrics (t) 
   
formula f :: ==
     Length (l)
   | Interval (l n n)
   | Element (w l) 
   | Mode (l) 
   | Sentiment (l) 
   | Style (t) 
   | Moods (t) 

statement S :: ==
     Print f S ; 
   | Print l S ;
   | Play  f S ;
   | Play  l S ;
   | 
    
```
How To use:
The two statements, Print and Play, will either print to the screen information about the queries or play the information (audio), respectively. 

Terms:
+ Songs are song titles
+ Artists are artist/band names
At the momment only title and names with only one space (max) are supported.
Using the 'and' term will allow you to chain multiple songs and/or artists, but note that all searchs will be conjunctive, so you may not get exactly what you want. Sometimes less is more.

Formulas to use:
+ Length will return a number that represents the number of words in the song.
+ Interval will return the lyrics between the two number inverals
+ Mode returns the most common word in a song
+ Sentiment uses IBM BlueMix Personality Insights to determine personality keywords to describe the song.
+ Style will return the style of music the term has
+ Moods will return the moods of music the term has (if there is one)

Statements:
+ Print will display the information on the screen
+ Play will play the information through your speackers


##Setup

```
git clone https://github.com/benlawson/MusicLingo.git
cd MusicLingo
virtualenv musicenv
source musicenv/bin/activate
pip install -r requirements.txt
wget http://people.bu.edu/balawson/key.txt #for IBM BlueMix credentials
python interpret.py
```

