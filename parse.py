####################################################################
#
# cas cs 320, fall 2015
# parse.py
# completed by ben lawson for musiclingo
#  ****************************************************************
#  @xxxx[{::::::::::::::>  PARSE THE STRINGS <::::::::::::::}]xxxx@ 
#  ****************************************************************
#

import re

def number(tokens, top = True):
    if re.compile(r"^(0|[1-9][0-9]*)*$").match(tokens[0]):
            return (int(tokens[0]), tokens[1:])

def variable(tokens, label = "Variable", top = True):
    if re.compile(r"^([A-Za-z0-9]|\s)+$").match(tokens[0]):
            return (tokens[0], tokens[1:])

def variable_wrapped(tokens, label = "Variable", top = True):
    if re.compile(r"^([A-Za-z0-9]|\s)+$").match(tokens[0]):
            return ({label:[tokens[0]]}, tokens[1:])

def word (tokens, top = True):
    return variable(tokens, label = 'word', top = True)

def tokenizeAndParse(s):
    tokens = tokenize(s)
    (p, tokens) =  statement(tokens)
    return p

def tokenize(s):
    s = s.lower()
    tokens = re.split(r"(\s+|print|play|length|lyrics|interval|styles|genre|element|both|mode|song|artist|and|sentiment|;|[[A-z]*\s[A-z]*|0-9]+)", s)
    good = []
    for t in tokens:
        good.extend(tokenizeword(t))
    tokens = [t.lower().strip() for t in good if not t.isspace() and not t == ""]
    return tokens 

def tokenizeword(s):
    s = s.lower()
    return  re.split(r"(print|play|length|lyrics|interval|styles|element|genre|both|mode|song|artist|and|sentiment|;|0-9]+)", s)
    
    

def parse(seqs, tmp, top = True):
    '''basic parser. this is taken from originally from the hw3 skeleton'''
    for (label, seq) in seqs:
        tokens = tmp[0:]
        (ss, es) = ([], [])
        for x in seq:
            if type(x) == type(""):
                if tokens[0] == x:
                    tokens = tokens[1:]
                    ss = ss + [x]
                else: break
            else:
                r = x(tokens, False)

def parse(seqs, tmp, top = True):
    '''basic parser. this is taken from originally from the hw3 skeleton'''
    for (label, seq) in seqs:
        tokens = tmp[0:]
        (ss, es) = ([], [])
        for x in seq:
            if type(x) == type(""):
                if tokens[0] == x:
                    tokens = tokens[1:]
                    ss = ss + [x]
                else: break
            else:
                r = x(tokens, False)
                if not r is None:
                    (e, tokens) = r
                    es = es + [e]
        if len(ss) + len(es) == len(seq) and (not top or len(tokens) == 0):
            return ({label:es} if len(es) > 0 else label, tokens)

def left(tmp, top = True):
    tokens = tmp[0:]
    if tokens[0] == 'song':
        return ({'Song' : [tokens[1]]}, tokens[2:])
    elif tokens[0] == 'artist':
        return ({'Artist' : [tokens[1]]}, tokens[2:])
    else: 
         return None

def term(tmp, top = True):
    tokens = tmp[0:]
    (e1, tokens) = left(tokens)
    if tokens and tokens[0] == 'and':
        (e2, tokens) = term(tokens[1:])
        return ({'And' :[e1, e2]}, tokens)
    else:
        return (e1, tokens)  

def formula(tmp, top = True):
    tokens = tmp[0:]
    r = parse([\
        ('Lyrics',  ['lyrics', '(',term, ')']),\
        ('Length',  ['length', '(', formula, ')']),\
        ('Mode',  ['mode', '(', formula, ')']),\
        ('Modes',  ['mode', '(', formula, number, ')']),\
        ('Sentiment',  ['sentiment', '(', formula, ')']),\
        ('Element',  ['element', '(', word, formula,  ')']),\
        ('Interval',  ['interval', '(', formula, number, number, ')']),\
        ('Styles',  ['styles',  '(', term, ')']),\
        ('Moods',  ['moods',  '(', term, ')']),\
        ('Genre',  ['genre',  '(', term, ')']),\
        ], tokens, top)
    if not r is None:
        return r

def statement(tmp, top = True):
    if len(tmp) == 0:
        return ('End', [])
    r = parse([\
        ('Print', ['print', formula, ';' , statement]),\
        ('Play',  ['play' , formula, ';' , statement]),\
        ('End', [])\
        ], tmp, top)
    if not r is None:
        return r
#eof
