#!/usr/bin/python

import cgi
import random

def htmlTop():
    print '''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <link rel="stylesheet" type="text/css" href="8ball.css">
            <title>Magic 8 Ball </title>
        </head>
        <body>
        <h1 id="heading"> Magic 8 ball</h1>
          <img src = "https://cdn.instructables.com/F9J/DI3G/ICRXU6YW/F9JDI3GICRXU6YW.LARGE.jpg" alt="Welcome" width = "100">
        <br>'''


def htmlTail():
    print '''</body>
        </html>'''

def getphrase():
    x = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it",
         "You can count on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
         "Absolutely", "Reply hazy try again", "Ask again later", "Better not tell you now",
         "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no",
         "My sources say no", "Outlook not so good", "Very doubtful", "Chances aren't good"]
    return x[random.randint(0,22)]
    
def main():
    htmlTop()
    print getphrase()
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
