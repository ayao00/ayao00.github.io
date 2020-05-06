#!/usr/bin/python

import cgi
import cgitb

cgitb.enable()

def htmlTop():
    print '''Content-type:text/html\n\n
          <!DOCTYPE html>
          <html lang="en-US">
                <head>
                        <meta charset="utf-8" />
                        <title> A Day in the Park </title>
                </head>
                <body>'''

def htmlTail():
    print '''</body>
            </html>'''

def convertToDict(fs):
    ans = dict()
    for key in fs:
        ans[key] = fs.getvalue(key)
    return ans


def main():
    formData = cgi.FieldStorage()
    data = convertToDict(formData)
    htmlTop()
    print '<h2> A Day in the Park </h2>'
    print '{name1} and {name2} were {verb1}ing in the park. Suddently, {noun1} appeared out of no where. They saw the {adjective1} {noun1} and immediately screamed. They {verb2} through the park and found a {adjective2} {noun2} to defend themselves. They never saw the {noun1} ever again.'.format(**data)
    htmlTail()
    


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
