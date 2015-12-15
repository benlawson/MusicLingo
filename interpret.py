exec(open('parse.py').read())
#exec(open('music.py').read())
exec(open('sentiment.py').read())
from music import *
from collections import Counter
import os

Node = dict
Leaf = str
Num = int

def evalTerm(env, t):
    if type(t) == Leaf: #word
        return t 

    if type(t) == Node:
        for label in t:
            children = t[label]
            if label == 'Artist':
                artist = children[0]
                return (artist, firstpage(artist, noun='artist') )
            if label == 'Song':
                song = children[0]
                return (song, firstpage(song, noun='song') )
            if label == 'And':
                e1 = children[0] 
                e2 = children[1] 
                v1 = evalTerm(env, e1)
                v2 = evalTerm(env, e2)
                joint = v1[0] + ' ' + v2[0]
                try:
                    return (joint, bothpage(v1[0], v2[1]))
                except:
                    pass
                try: 
                    return (joint, bothpage(v1[1], v2[0]))
                except:
                    return (joint, firstpage(joint, noun='song') )

def evalNumber(env, t):
    if type(t) == Num:
         return t 
            
def evalLyrics(env, t):
    if type(t) == Node:
        for label in t:
            children = t[label]
            if label == 'Lyrics':
                f1 = children[0]
                v1 = evalTerm(env, f1)[1]
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
                v1 = evalLyrics(env, f1)
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
            elif label == 'Element':
                f1 = children[0]
                f2 = children[1]
                v1 = evalTerm(env, f1)[1]
                v2 = evalLyrics(env, f2)
                return v1 in v2
            elif label == 'Moods':
                f1 = children[0]
                v1 = evalTerm(env, f1)[1]
                return secondpage(v1, adjective='moods') 
            elif label == 'Styles':
                f1 = children[0]
                v1 = evalTerm(env, f1)[1]
                return secondpage(v1, adjective='styles') 
            elif label == 'Genre':
                f1 = children[0]
                v1 = evalTerm(env, f1)[1]
                return secondpage(v1, adjective='genre') 

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
                if type(v) == type(None):
                    v = evalLyrics(env, f)
                    lyrics = True
                else: lyrics = False
                (env, o) = execStatement(env, S)
                if lyrics:
                    v = [str(x) for x in v]
                    v = ' '.join(v).replace("\r",' ').replace("\n",' ')
                return (env, [v] + o)
            if label == 'Play':
                children = s[label]
                f = children[0]
                S = children[1]
                v = evalFormula(env, f)
                if type(v) == type(None):
                    v = evalLyrics(env, f)
                    lyrics = True
                else: lyrics = False
                (env, o) = execStatement(env, S)
                if lyrics: 
                    v = [str(x) for x in v]
                    v = ' '.join(v).replace("\r",' ').replace("\n",' ').replace('\'', '')
                os.popen('say {0}'.format([str(v) + str(o)]))
                return (env, ['you should hear this'] + o)

def interpret(s):
    tokens = tokenizeAndParse(s)
    (env, o) = execStatement({}, tokens)
    return o

def interact(s=''):
    prompt = '>'
    while True:
        # Prompt the user for a query.
        s = raw_input('{0} '.format(prompt))
        if ':quit' in s or ':exit' in s or ':q' in s:
            break

        if s.split(' ')[0] == ':set':
            prompt = ' '.join(s.split(' ')[1:])+ '>' #easter egg
            continue
        # Parse and evaluate the query.
        try: 
            print interpret(s)
        except: 
           print("Something went wrong. Check the syntax?")
 
if __name__ == "__main__": 
    interact()

#eof
