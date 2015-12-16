#####################################################################
# analyze.py

exec(open('parse.py').read())

Node = dict
Leaf = str
Num = int

def typeTerm(e):
    if type(e) == Leaf:
        return 'TyString'
    if type(e) == Num: 
        return 'TyNumber'

    if type(e) == Node:
        for label in e:
            children = e[label]

            if label == 'Artist' or label == 'Song':
                f1 = children[0]
                v1 = typeTerm(f1) 
                if v1 == 'TyString':
                    return 'TyString'  
                
            elif label == 'And':
                f1 = children[0]
                f2 = children[1]
                v1 = typeTerm(f1)
                v2 = typeTerm(f2)
                return 'TyString' if v1 == v2 == 'TyString' else None

def typeFormula(s):
    if type(s) == Node:
        for label in s:
            children = s[label]
            if label in ['Length', 'Mode', 'Sentiment']:
                f = children[0] 
                v = typeFormula(f)
                if v == 'TyString':
                    return 'TyString'
                else: 
                   return None 
            elif label in [ 'Genre', 'Moods', 'Styles', 'Lyrics']: 
                f = children[0] 
                v = typeTerm(f)
                if v == 'TyString':
                    return 'TyString'
                else: return None 
            elif label == 'Interval':
                f1 = children[0]
                f2 = children[1]
                f3 = children[2]
                v1 = typeFormula(f1)
                v2 = typeTerm(f2)
                v3 = typeTerm(f3)
                return 'TyString' if v1 == 'TyString' and v2 == v3 == 'TyNumber' else None
            elif label == 'Element':
                f1 = children[0]
                f2 = children[1]
                v1 = typeTerm(f1)
                v2 = typeFormula(f2)
                return 'TyString' if v1 == v2 == 'TyString' else None
            elif label == 'Modes':
                f1 = children[0]
                f2 = children[1]
                v1 = typeFormula(f1)
                v2 = typeTerm(f2)
                return 'TyString' if v1 == 'TyString' and v2 == 'TyNumber' else None


def typeStatement(s):
    if type(s) == Leaf:
        if s == 'End':
            return 'TyVoid'
    
    elif type(s) == Node:
        for label in s:
            if label == 'Print' or label == 'Play':
                [e, p] = s[label]
                n = typeFormula( e)
                p1 = typeStatement( p)
                if n == 'TyString' and p1 == 'TyVoid':
                    return 'TyVoid' 

#eof
