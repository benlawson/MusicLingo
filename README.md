#Music

####by Ben Lawson
==================

The goal of this project is to create an easier way to manipultate music and query it. This language uses data generated from the user-contributed website [allmusic.com](allmusic.com). The print statement prints to screen and the play function will read aloud the results through your speakers. Deadcode elimination will short circuit poorly phrased queries to return the expected 'None' before the query reaches the server. 

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

Example of a nested statement (note the structure of the output, a 2-element list)
```
>print genre ( artist taylor swift and song love story) ; print styles ( artist taylor swift and song love story ) ; 
['Country Pop/Rock', 'Contemporary_Country Country-Pop Pop']
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
+ Styles will return the style of music the term has
+ Element will return a boolean if the word is in the lyrics 
+ Moods will return the moods of music the term has (if there is one)
+ Genre will return the genre of the music

Statements:
+ Print will display the information on the screen
+ Play will play the information through your speakers


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


######Easter Eggs
in the MusicLingo shell you can change the prompt with the command
```
MusicLingo>:set <expression> 
<expression>>
```
