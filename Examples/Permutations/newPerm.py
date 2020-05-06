#!/usr/bin/python

import cgi
import cgitb
import itertools

cgitb.enable()

def htmlTop():
    print '''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
             <link rel="stylesheet" type="text/css" href="mystyle.css">
            <title> Permutations </title>
        </head>
        <body>'''


def htmlTail():
    print '''</body>
        </html>'''
    
def getData():
    formData = cgi.FieldStorage()
    givenword = formData.getvalue('givenword')
    return givenword

def main():
    htmlTop()
    word = getData().lower()
    if len(word) > 7:
        print'''Word is too long. Please return to <a href="http://homer.stuy.edu/~ayao00/Examples/Permutations/Permutations.html">Permutations Homepage</a>'''
    print "<h3>Permutations</h3><br>"
    n = 1
    for w in itertools.permutations(word):
            print "{}.".format(n)+"".join(list(w))+"<br>"
            n += 1
    print "<h3>Anagrams</h3><br>"
    anagrams = []
    fh = open("/etc/dictionaries-common/words",'r')
    fileRead = fh.readlines()
    for line in fileRead:
        anagrams += line.split()
    fileRead = map(lambda x: x.strip(',!.?'), anagrams)
    x = []
    n = 1
    for w in itertools.permutations(word):
        v = "".join(list(w))
        if v in fileRead:
            x.append(v)
##            print "{}.".format(n)+ v
    x = list(set(x))
    for h in x:
        print "{}.".format(n)+ h
        n += 1
    fh.close()
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
