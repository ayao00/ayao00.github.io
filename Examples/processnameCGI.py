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
                        <title> Process Full Name </title>
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
    1d,2d,3d,4d,5d,6d,7d,8d="{1d}".format(**data),"{2d}".format(**data),"{3d}".format(**data),"{4d}".format(**data),"{5d}".format(**data),"{6d}".format(**data),"{7d}".format(**data),"{8d}".format(**data),
    1r,2r,3r,4r,5r,6r="{1r}".format(**data),"{2r}".format(**data),"{3r}".format(**data),"{4r}".format(**data),"{5r}".format(**data),"{6r}".format(**data)
    1m,2m,3m="{1m}".format(**data),"{2m}".format(**data),"{3m}".format(**data)
    fh=open("Dataset.csv",'r')
    fhread= fh.readlines()
    readline = []
    for lines in fhread:
        readline += [lines.split(",")]
    if 1d == "true":
        for x in readline:
            if x[0] = "2007":
                print " ".join(x)
    fh.close()
    htmlTail()
    


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
