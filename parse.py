#####################################################################
#
# cas cs 320, fall 2015
# midterm (skeleton code)
# parse.py
# completed by ben lawson
#  ****************************************************************
#  @xxxx[{::::::::::::::>  PARSE THE STRINGS <::::::::::::::}]xxxx@ 
#  ****************************************************************
#

import re

def number(tokens, top = True):
    if re.compile(r"^(0|[1-9][0-9]*)*$").match(tokens[0]):
            return ({'Number':[int(tokens[0])]}, tokens[1:])

def variable(tokens, label = "Variable", top = True):
    if re.compile(r"^[A-Za-z0-9]+$").match(tokens[0]):
            return ({label:[tokens[0]]}, tokens[1:])
def song (tokens, top):
    return variable(tokens, label = 'Song', top = True)
def artist (tokens, top):
    return variable(tokens, label = 'Artist', top = True)

def tokenizeAndParse(s):
    tokens = re.split(r"(\s+|:=|print|play|\+|length|lyrics|interval|style|element|both|{|}|;|\[|\]|,|@|\$)", s)
    tokens = [t for t in tokens if not t.isspace() and not t == ""]
    print tokens
    (p, tokens) =  statement(tokens)
    return p

def parse(seqs, tmp, top = True):
    '''basic parser. this is taken from orginally from the hw3 skeleton'''
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

def formula(tmp, top = True):
    tokens = tmp[0:]
    r = parse([\
        ('Length',  ['length', '(', song, ')']),\
        ('Lyrics',  ['lyrics', '(', song, ')']),\
        ('Interval',  ['interval', '(', song, number, number, ')']),\
        ('Style',  ['style',  '(', term, ')']),\
        ('Both',  ['both', '(', 'Artist', '(', song, song, ')'])\
        ], tmp, top)
    if not r is None:
        return r

def term(tmp, top = True):
    tokens = tmp[0:]
    if tokens[0] == 'Artist':
        return artist(tokens[1])
    else:
        return song(tokens[0])
     
def statement(tmp, top = True):
    if len(tmp) == 0:
        return ('End', [])
    r = parse([\
        ('Print', ['print', '(' ,formula, ')', statement]),\
        ('Play',  ['play' , '(' ,formula, ')', statement]),\
        ('End', [])\
        ], tmp, top)
    if not r is None:
        return r
#eof
