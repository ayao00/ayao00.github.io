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
                        <title> Quiz Results </title>
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
    print 'Q1.{Q1}<br> Q2.{Q2}<br> Q3.{Q3}<br> Q4.{Q4}<br> Q5.{Q5}<br> Q6.{Q6}<br> Q7.{Q7}<br> Q8.{Q8}<br> Q9.{Q9}<br> Q10.{Q10}<br>'.format(**data)
    score = ["{Q1}".format(**data),"{Q2}".format(**data),"{Q3}".format(**data),"{Q4}".format(**data),"{Q5}".format(**data),"{Q6}".format(**data),"{Q7}".format(**data),"{Q8}".format(**data),"{Q9}".format(**data),"{Q10}".format(**data)].count("correct")
    if score >= 8:
        print "Congrats! You got a "+str(score)+" out of 10."
    if score >=5 and score <8:
        print "Better luck next time! You got a "+str(score)+" out of 10"
    if score < 5:
        print "Sorry! You only got a "+str(score)+" out of 10. Here is a link to help you review:<a href='https://pclt.sites.yale.edu/introduction-pc-hardware'>Introduction to PC hardware</a>"
    htmlTail()
    


if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
