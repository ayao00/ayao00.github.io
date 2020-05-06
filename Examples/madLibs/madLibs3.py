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
                        <title> A Day in School </title>
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
    print "<h3> A Day in School </h3>"
    print 'In the morning, {1n} sees {2n} and goes to say hi. They {1v} to school but to find a {1no} in their first period class. It was a very {1adj} {1no}. They did not know what to do with it so they left it. A teacher came {2v}ing into class. She looked extremely agitated. She held a {2no} in one hand and a note in the other. She seemed to be having a {2adj} day so {1n} and {2n} suggested that she just dismissed them. She agreed and both of them waltzed out.'.format(**data)
    htmlTail()
    


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
