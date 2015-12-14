exec(open('parse.py').read())
exec(open('music.py').read())
exec(open('sentiment.py').read())

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
                return data.most_common(1)[0][0]
            elif label == 'Sentiment':
                f1 = children[0]
                v1 = evalLyrics(env, f1)
                return personality_insights(v1)  
    elif type(f) == Leaf:
        if f == 'True':
            return 'True'
        if f == 'False':
            return 'False'

def evalExpression(env, s): # Useful helper function.
    v1 = evalTerm(env, s)
    if v1:
        return v1
    else: return (evalFormula(env,s))

def execProgram(env, s):
    if type(s) == Leaf:
        if s == 'End':
            return (env, [])
    elif type(s) == Node:
        for label in s:
            if label == 'Print':
                children = s[label]
                f = children[0]
                p = children[1]
                v = evalFormula(env, f)
                if not(v):
                    v = evalTerm(env, f)
                (env, o) = execProgram(env, p)
                return (env, [v] + o)
            if label == 'Assign':
                children = s[label]
                x = children[0]['Variable'][0]
                f = children[1]
                p = children[2]
                v = evalExpression(env, f)
                env[x] = v
                (env, o) = execProgram(env, p)
                return (env, o)
            if label == 'Procedure':
                children = s[label]
                x = children[0]['Variable'][0]
                p = children[1]
                r = children[2]
                env[x] = p 
                (env, o) = execProgram(env, r)
                return (env, o)
            if label == 'Call':
                children = s[label]
                x = children[0]['Variable'][0]#access variable
                r = children[1]#rest
                p = env[x] #procedure in env
                (env2, o1) = execProgram(env, p)
                (env3, o2) = execProgram(env2, r)
                return (env3, o1 + o2)
            if label == 'Until':
                children = s[label]
                exp  = children[0]
                body = children[1]
                rest = children[2]
                env1 = env
                v = evalFormula(env1,exp)
                if v == 'True':
                    (env3, o2) = execProgram(env1, rest)
                if v == 'False':
                    (env3, o2) = execProgram(env1, {'Until':[body, exp, rest]})
                return (env3,  o2)
            if label == 'If':
                children = s[label]
                f1 = children[0]
                f3 = children[2]
                v1 = evalFormula(env, f1)
                if v1 == None:
                    v1 = evalTerm(env, f1)
                if v1 == 'True': 
                    f2 = children[1]
                    env,o = execProgram(env, f2)
                env,o2 = execProgram(env, f3)
                return (env, o + o2)

def interpret(s):
    (env, o) = execProgram({}, tokenizeAndParse(s))
    return o

#eof
