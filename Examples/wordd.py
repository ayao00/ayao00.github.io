#!/usr/bin/python

import cgi
import itertools

def htmlTop():
    print '''Content-type:text/html\n\n
          <!DOCTYPE html>
          <html lang="en-US">
                <head>
                        <meta charset="utf-8" />
                        <title> Process Name </title>
                </head>
                <body>
                '''

def htmlTail():
    print '''</body>
            </html>'''

def getData():
    formData = cgi.FieldStorage()
    word = formData.getvalue('word')
    return word

def main():
    htmlTop()
    word = getData()
    if len(word) > 7:
        print alert("Word is too long")
    n = 1
    fileIn = open("/etc/dictionaries-common/words",'r')
    fileRead = fileIn.readlines()
    fileRead.split()
    fileRead = map(lambda x: x.strip(',!.?'), fileRead)
    for w in itertools.permutations(word):
        if w in fileRead:
            print "{}."+ w
        n += 1
    fileIn.close()
    htmlTail()
    


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
