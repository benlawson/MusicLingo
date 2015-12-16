#MusicLingo

####by Ben Lawson
==================

The goal of this project is to create an easier way to manipultate music and query it. This language uses data generated from the user-contributed website [allmusic.com](http://www.allmusic.com). The print statement prints to screen and the play function will read aloud the results through your speakers. A simple query optimizer will reduce the number of calls made to the website, by elimating 'null code', code that wouldn't recieve a response anyways.  

##Sample Queries
First, start the MusicLingo interpretor by running the following. Additional setup intructions can be found [here](https://github.com/benlawson/MusicLingo#setup)
```
python interpret.py 
```
Print a the most common word of a random song by Adele
```
MusicLingo> print mode ( lyrics ( song adele ) ) ;
['had']
```
You can also pass in a number to find X number of most common words
```
MusicLingo> print mode ( lyrics ( song hello ) 10 ) ;
["you a to (hello hello) I'll lonely that all she"]

```

Print the most common word in the song 'Hello' by Adele
```
MusicLingo> print mode ( lyrics ( artist adele and song hello ) ) ;
['you']
```

Print the lengh of the song Hotline Bling
```
MusicLingo> print length ( lyrics ( song hotline bling ) ) ;
[373]
```

Print the 'personality' of the song Hello by Adele
```
MusicLingo>print sentiment ( lyrics ( artist adele and song hello ) ) ;
[[u'Orderliness', u'Assertiveness', u'Excitement-seeking', u'Gregariousness']]
```
Check if a word is in the lyrics
```
MusicLingo>print element ( hate lyrics ( artist taylor swift and song love ) ) ;
[True]
```

Check the moods of an artist or song
```
MusicLingo>print moods ( artist taylor swift ) ;
 ['Cathartic Earnest Passionate Sentimental Warm Exuberant Reflective Sophisticated Carefree Confident Gentle Laid-Back/Mellow Organic Playful Refined Springlike Sweet Yearning Amiable/Good-Natured Bittersweet Cheerful Confrontational Theatrical Angst-Ridden Relaxed Romantic Clinical Effervescent Poignant']
```
Check the styles of an artist or song
```
MusicLingo>print styles ( artist taylor swift and song love story) ;
['Contemporary_Country Country-Pop Pop']
```

Check the genre of an artist or song
```
MusicLingo>print genre ( artist taylor swift and song love story) ;
['Country Pop/Rock']
```

Example of a joined statement (note the structure of the output, a 2-element list)
```
MusicLingo>print genre ( artist taylor swift and song love story) ; print styles ( artist taylor swift and song love story ) ; 
['Country Pop/Rock', 'Contemporary_Country Country-Pop Pop']
```

Play statement: works on Mac or Linux with *gnustep-gui-runtime* package installed
on Debian-based systems you install via:
```
sudo apt-get install gnustep-gui-runtime
```

```
MusicLingo>play lyrics (artist adele and song hello ) ;
['you should hear this']
```

Play just the first 100 words of song: 
```
MusicLingo>play interval ( lyrics ( artist taylor swift and song love ) 0 100 ) ;
['you should hear this']
```

##BNF Notation for the MusicLingo language

```
number n :: == natural numbers 
word   w :: == an English word, song, or artist

term t :: ==
     left 
   | left and t

left :: ==
     Song w
   | Artist w
     
formula f :: ==
     Lyrics (t) 
   | Length (f)
   | Interval (f n n)
   | Element (w f) 
   | Mode (f) 
   | Mode (f n) 
   | Sentiment (f) 
   | Style (t) 
   | Moods (t) 
   | Genre (t) 

statement S :: ==
     Print f ; S
   | Play  f ; S
   | 
    
```

##How To use:

###Terms:
+ Songs are song titles
+ Artists are artist/band names


At the momment only title and names with only one space (max) are supported.
Using the 'and' term will allow you to chain multiple songs and/or artists, but note that all searchs will be conjunctive, so you may not get exactly what you want. Sometimes less is more.

###Lyrics:
+ use this will term to query the lyrics of a specific one or a random one from a an artist. 

###Formulas:
+ Length will return a number that represents the number of words in the lyrics.
+ Interval will return the lyrics between the two number inverals
+ Mode returns the most common word in the lyrics
+ Mode (N), returns the most common N words in lyrics
+ Sentiment uses IBM BlueMix Personality Insights to determine personality keywords to describe the lyrics
+ Styles will return the style of music the term has
+ Element will return a boolean if the word is in the lyrics 
+ Moods will return the moods of music the term has (if there is one)
+ Genre will return the genre of the music

###Statements:
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


######Easter Egg
in the MusicLingo shell you can change the prompt with the command
```
MusicLingo>:set new_string
new_string>
```

######Future Goals?
I want to be able to add in a few more control flow operations ( If/Then ) that could interact with the boolean 'Element' formula, but I don't think I'll have time.  
