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
    1m,2m,3m = "{1m}".format(**data),"{2m}".format(**data),"{3m}".format(**data)
    fh=open("Dataset.csv",'r')
    fhread= fh.readlines()
    readline = []
    for lines in fhread:
        readline += [lines.split(",")]
    if 1d == "true":
        for x in readline:
            if x[0] == "2007":
                print " ".join(x)
    if 2d == "true":
        for x in readline:
            if x[0] == "2008":
                print " ".join(x)
    if 3d == "true":
        for x in readline:
            if x[0] == "2009":
                print " ".join(x)
    if 4d == "true":
        for x in readline:
            if x[0] == "2010":
                print " ".join(x)
    if 5d == "true":
        for x in readline:
            if x[0] == "2011":
                print " ".join(x)
    if 6d == "true":
        for x in readline:
            if x[0] == "2012":
                print " ".join(x)
    if 7d == "true":
        for x in readline:
            if x[0] == "2013":
                print " ".join(x)
    if 8d == "true":
        for x in readline:
            if x[0] == "2014":
                print " ".join(x)
    if 1r == "true":
        for x in readline:
            if x[3] == "Black Non-Hispanic":
                print " ".join(x)
    if 2r == "true":
        for x in readline:
            if x[3] == "Asian and Pacific Islander":
                print " ".join(x)
    if 3r == "true":
        for x in readline:
            if x[3] == "Hispanic":
                print " ".join(x)
    if 4r == "true":
        for x in readline:
            if x[3] == "White Non-Hispanic":
                print " ".join(x)
    if 5r == "true":
        for x in readline:
            if x[3] == "Other Race/Ethnicity":
                print " ".join(x)
    if 6r == "true":
        for x in readline:
            if x[3] == "Not Stated/Unknown":
                print " ".join(x)
    if 1m == "true":
        deaths= filter(lambda x: x[4], readline)
        deaths.sort(-1)
        print deaths[0:10]
    if 2m == "true":
        DeathRates = filter(lambda x: x[5], readline)
        DeathRates.sort(-1)
        print DeathRates[0:10]
    if 3m == "true":
        AADR = filter(lambda x: x[6], readline)
    
    fh.close()
    htmlTail()
    


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
