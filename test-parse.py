import re

############################################################
# Load the files. Change the path if necessary.

exec(open('parse.py').read())

def check(name, function, inputs_result_pairs):
    def str_(s):
        return '"'+str(s)+'"' if type(s) == str else str(s)
    if type(name) == tuple:
        prefix = name[0]
        suffix = name[1]
    if type(name) == str:
        prefix = name + '('
        suffix = ')'

    passed = 0
    for (inputs, result) in inputs_result_pairs:
        try:
            output = function(inputs[0], inputs[1]) if len(inputs) == 2  else function(inputs[0])
        except:
            output = '<Error>'

        if output != '<Error>' and output == result:
            passed = passed + 1
        else:
            print("\n  Failed on:\n    "+prefix+', '.join([str_(i) for i in inputs])+suffix+"\n\n"+"  Should be:\n    "+str_(result)+"\n\n"+"  Returned:\n    "+str_(output)+"\n")
    print("Passed " + str(passed) + " of " + str(len(inputs_result_pairs)) + " tests.")
    print("")

############################################################
# The tests.


print("number()...")
try: number
except: print("The number() function is not defined.")
else: check('number', number, [\
    ((["123"],), (123, [])),\
    ((["0"],), (0, [])),\
    ((["1010"],), (1010, [])),\
    ((["-1010"],), None),\
    ((["a45"],), None),\
    ((["abc"],), None),\
    ])

print("word()...")
try: word
except: print("The word() function is not defined.")
else: check('song', word, [\
    ((["Hello"],), ('Hello', [])),\
    ((["What do you mean"],), ("What do you mean", [])),\
    ((["-1010"],), None),\
    ((["a45"],), ("a45", [])),\
    ])

print("term()...")
try: term
except: print("The term() function is not defined.")
else: check('term', term, [\
    (("artist adele".split(" "),), ({'Artist':["adele"]}, [])),\
    (("artist emiemem".split(" "),), ({'Artist':["emiemem"]}, [])),\
    (("song hello".split(" "),), ({'Song':['hello']}, [])),\
    (("artist adele and song hello".split(" "),), ({'And': [{'Artist': ['adele']}, {'Song': ['hello']}]}, [])),\
    ])

print("lyrics()...")
try: lyrics 
except: print("The lyrics() function is not defined.")
else: check('lyrics', lyrics, [\
    (("lyrics ( artist adele )".split(" "),), ({'Lyrics' : [{'Artist': ['adele']}]}, [])),\
    (("lyrics ( song hello )".split(" "),), ({'Lyrics' : [{'Song': ['hello']}]}, [])),\
    ])

print("formula()...")
try:  formula
except: print("The formula() function is not defined.")
else: check('formula', formula, [\
    (("length ( lyrics ( artist adele ) )".split(" "),), ({'Length' : [{'Lyrics' : [{'Artist': ['adele']}]}]}, [])),\
    (("interval ( lyrics ( artist adele ) 0 2 )".split(" "),), ({'Interval': [{'Lyrics': [{'Artist': ['adele']}]}, 0, 2]}, [])),\
    ((["moods", "(", "artist", "taylor swift", ")"],), ({'Moods' : [{'Artist': ['taylor swift']}]}, [])),\
    (("mode ( lyrics ( artist adele and song hello ) )".split(" "),), ({'Mode' : [{'Lyrics' : [{'And' :[{'Artist': ['adele']}, {'Song' :['hello']}]}]}]}, [])),\
    ])

print("statement()...")
try: statement 
except: print("The statement() function is not defined.")
else: check('statement', statement, [\
    (("print lyrics ( song hello ) ;".split(" "),), ({'Print': [{'Lyrics' : [{'Song': ['hello']}]}, 'End']}, [])),\
    (("123 ;".split(" "), True), None),\
    (("123 + 456".split(" "), True), None),\
    (("if { print true ; }".split(" "), True), None),\
    ])
#eof
