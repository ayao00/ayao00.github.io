#!/usr/bin/python

import cgi

def htmlTop():
    print '''Content-type:text/html\n\n
          <!DOCTYPE html>
          <html lang="en-US">
                <head>
                        <meta charset="utf-8" />
                        <title> Process Name </title>
                </head>
                <body>'''

def htmlTail():
    print '''</body>
            </html>'''

def getData():
    formData = cgi.FieldStorage()
    word = formData.getvalue('word')
    if len(word) > 7:
    return word


def main():
    htmlTop()

    htmlTail()
    


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
