exec(open('parse.py').read())
#exec(open('music.py').read())
exec(open('sentiment.py').read())
exec(open('optimize.py').read())
#exec(open('analyze.py').read())
from analyze import * 
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
                if song:
                    return (song, firstpage(song, noun='song') )
                else: 
                    return (song, None)
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
            
def evalFormula(env,f):
    if type(f) == Node:
        for label in f:
            children = f[label]
            if label == 'Length':
                f = children[0]
                f1 = evalFormula(env, f)
                return len(f1.split(' '))  
            elif label == 'Interval':
                f1 = children[0]
                f2 = children[1]
                f3 = children[2]
                v1 = evalFormula(env, f1)
                v2 = evalNumber(env, f2)
                v3 = evalNumber(env, f3)
                return ' '.join((filter(lambda d: len (d) > 0, v1.split(' ')[v2:v3])))
            elif label == 'Mode':
                f1 = children[0]
                v1 = evalFormula(env, f1)
                try:
                    v1 = v1.split(' ')
                except:
                    pass
                data = Counter(v1)
                return  str(data.most_common(1)[0][0])
            elif label == 'Modes':
                f1 = children[0]
                f2 = children[1]
                v1 = evalFormula(env, f1)
                v2 = evalNumber(env, f2)
                try:
                    data = Counter(filter(lambda d: len (d) > 0, v1.split(' ')))
                except:
                    data = Counter(v1)
                x =  ' '.join([str(x) for x in list(zip(*data.most_common(v2))[0])]) #might break in Python3 (zip function)
                return x
            elif label == 'Sentiment':
                f1 = children[0]
                v1 = evalFormula(env, f1)
                return personality_insights(v1)  
            elif label == 'Element':
                f1 = children[0]
                f2 = children[1]
                v1 = evalTerm(env, f1)[1]
                v2 = evalFormula(env, f2)
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
            elif label == 'Lyrics':
                f1 = children[0]
                v1 = evalTerm(env, f1)[1]
                if v1:
                    v = secondpage(v1, adjective='lyrics') 
                    v = [str(x) for x in v]
                    v = ' '.join(v).replace("\r",' ').replace("\n",' ').replace('\'', '')           
                    return v
                else:
                    return None 

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
                (env, o) = execStatement(env, S)
                os.popen('say {0}'.format([str(v) + str(o)]))
                return (env, ['you should hear this'] + o)

def interpret(s):
    tree = tokenizeAndParse(s)
    tree2 = eliminateDeadCode(tree) 
    if typeStatement(tree2)  == 'TyVoid':
        (env, o) = execStatement({}, tree2)
        return o
    else:
        return 'Not typed correctly'

def interact(s=''):
    prompt = 'MusicLingo>'
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
