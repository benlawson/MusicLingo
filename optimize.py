#####################################################################
# optimize.py
#
Node = dict
Leaf = str
Num  = int

def eliminateDeadCode(s):
    if type(s) == Leaf or type(s) == Num:
        return s
    if type(s) == Node:
        for label in s:
            children = s[label]
            if label == 'Print':
                [e, p] = children
                return {'Print':[eliminateDeadCode(e), eliminateDeadCode(p)]}
            elif label == 'Play':
                [e, p] = children
                return {'Play': [eliminateDeadCode(e), eliminateDeadCode(p)]}

            elif label == 'And':
                [e1, e2] = children
                for label in e1:
                    if label == 'Song':
                        for label in e2:
                            if label == 'Song':
                                return {'Song' : ['']} 
                return {'And':children}            
            
            return {label : [eliminateDeadCode(c) for c in children]}

#eof
