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
                        <title> A Day in a Haunted House </title>
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
    print '<h2> A Day in a Haunted House</h2>'
    print '{firstname} decided to go to a haunted house one day. When they entered the haunted hosue, they heard voices inside. They were terrified at first but then met a {firstadjective} {firstnoun} named {secondname}. At first, {firstname} ran but then approached the {firstadjective} {firstnoun}. {secondname} started to {secondverb} and {firstname} found it fun. {secondname} had a special ability and made a {secondnoun} appear.  The day in the haunted house was {secondadjective}.'.format(**data)
    htmlTail()
    


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
