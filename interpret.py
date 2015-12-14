exec(open('parse.py').read())
exec(open('music.py').read())
exec(open('sentiment.py').read())
#from music import *
from collections import Counter

Node = dict
Leaf = str

def evalTerm(env, t):
    if type(t) == Leaf: #song
        return firstpage(t, noun='song') 

    if type(t) == Node:
        for label in t:
            children = t[label]
            if label == 'Artist':
                artist = children[0]
                return firstpage(artist, noun='artist') 
            if label == 'Song':
                song = children[0]
                return firstpage(song, noun='song') 
            if label == 'Both':
                artistNode = children[0]
                song = children[1]['Song'][0]
                artisturl = evalTerm(env, artistNode)
                return bothpage(artisturl, song) 

def evalNumber(env, t):
    if type(t) == Node:
        for label in t:
            children = t[label]
            if label == 'Number':
                return children[0]
            
def evalLyrics(env, t):
    if type(t) == Node:
        for label in t:
            children = t[label]
            if label == 'Lyrics':
                f1 = children[0]
                v1 = evalTerm(env, f1)
                return secondpage(v1, adjective='lyrics') 
         
def evalFormula(env,f):
    if type(f) == Node:
        for label in f:
            children = f[label]
            if label == 'Length':
                f = children[0]
                f1 = evalLyrics(env, f)
                return len(f1)  
            elif label == 'Interval':
                f1 = children[0]
                f2 = children[1]
                f3 = children[2]
                v1 = evalLyrics(env, f1)[0]
                v2 = evalNumber(env, f2)
                v3 = evalNumber(env, f3)
                return v1[v2:v3]
            elif label == 'Mode':
                f1 = children[0]
                v1 = evalLyrics(env, f1)
                data = Counter(v1)
                return str(data.most_common(1)[0][0])
            elif label == 'Sentiment':
                f1 = children[0]
                v1 = evalLyrics(env, f1)
                return personality_insights(v1)  
            elif label == 'Sentiment':
                f1 = children[0]
                v1 = evalTerm(env, f1)

def execStatement(env, s):
    if type(s) == Leaf:
        if s == 'End':
            return (env, [])
    elif type(s) == Node:
        for label in s:
            if label == 'Print':
                children = s[label]
                f = children[0]
                S = children[1]
                v = evalFormula(env, f)
                (env, o) = execStatement(env, S)
                return (env, [v] + o)
            if label == 'Play':
                children = s[label]
                f = children[0]
                S = children[1]
                v = evalFormula(env, f)
                (env, o) = execStatement(env, p)
                return (env, o)

def interpret(s):
    tokens = tokenizeAndParse(s)
    (env, o) = execStatement({}, tokens)
    return o

def interact(s):
    while True:
        # Prompt the user for a query.
        s = input('> ')
        if s == ':quit':
            break

        # Parse and evaluate the query.
        try: 
            tokens = tokenizeAndParse(s)
            if not tokens is None:
                (env, o) = execStatement({}, tokens)
                print o
            else:
                print("Unknown input.")
        except TypeError:
            print("Incorrect syntax.")
 


#eof
