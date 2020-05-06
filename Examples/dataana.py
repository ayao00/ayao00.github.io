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
                        <title> Data Results </title>
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

##def getData(x):
##    formData = cgi.FieldStorage()
##    name = formData.getvalue(str(x))
##    return name

def main():
    formData = cgi.FieldStorage()
    data = convertToDict(formData)
    htmlTop()
    print '''<h3> Analysis Results </h3>
            <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>
            '''
    fh=open("Dataset.csv",'r')
    fhread= fh.readlines()
    readline = []
    for lines in fhread:
        readline += [lines.split(",")]
    if "1d" in data:
        print "<h3> Leading Causes 2007 </h3>"
        for x in readline:
            if x[0] == "2007":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"        
    if "2d" in data:
        print '''<h3> Leading Causes 2008 </h3>
                <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>'''
        for x in readline:
            if x[0] == "2008":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"            
    if "3d" in data:
        print '''<h3> Leading Causes 2009 </h3>
                <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>'''
        for x in readline:
            if x[0] == "2009":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"            
    if "4d" in data:
        print '''<h3> Leading Causes 2010 </h3>
                <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>'''
        for x in readline:
            if x[0] == "2010":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"
    if "5d" in data:
        print '''<h3> Leading Causes 2011 </h3>
                <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>'''
        for x in readline:
            if x[0] == "2011":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"
    if "6d" in data:
        print '''<h3> Leading Causes 2012 </h3>
                <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>'''
        for x in readline:
            if x[0] == "2012":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"
    if "7d" in data:
        print '''<h3> Leading Causes 2013 </h3>
                <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>'''
        for x in readline:
            if x[0] == "2013":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"
    if "8d" in data:
        print '''<h3> Leading Causes 2014 </h3>
                <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>'''
        for x in readline:
            if x[0] == "2014":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"
    if "1r" in data:
        print '''<h3>Leading Causes for Black Non-Hispanics</h3>
        <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>'''
        for x in readline:
            if x[-4] == "Black Non-Hispanic":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"
    if "2r" in data:
        print '''<h3>Leading Causes for Asian and Pacific Islanders</h3>
        <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>'''
        for x in readline:
            if x[-4] == "Asian and Pacific Islander":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"
    if "3r" in data:
        print '''<h3>Leading Causes for Hispanics</h3>
                <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>'''
        for x in readline:
            if x[-4] == "Hispanic":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"
    if "4r" in data:
        print '''<h3>Leading Causes for White Non-Hispanics</h3>
                <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>'''
        for x in readline:
            if x[-4] == "White Non-Hispanic":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"
    if "5r" in data:
        print '''<h3>Leading Causes for Other Race/Ethnicity</h3>
                <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>'''
        for x in readline:
            if x[-4] == "Other Race/ Ethnicity":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"
    if "6r" in data:
        print '''<h3>Leading Causes for Not Stated/Unknown</h3>
                <table align="center">
                <tr>
                    <th>Year </th>
                    <th>Leading Cause </th> 
                    <th>Sex </th>
                    <th>Race Ethnicities </th>
                    <th>Deaths</th>
                    <th>Death Rate</th>
                    <th>Age Adjusted Death Rate</th>
                </tr>'''
        for x in readline:
            if x[-4] == "Not Stated/Unknown":
                if x.count(",") < 7:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
                else:
                    print '<tr>'+'<td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td>'.format(x[0], x[1:-6], x[-5], x[-4], x[-3], x[-2], x[-1])+'</tr>'
        print "</table>"
    fh.close()
    htmlTail()
	    


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
