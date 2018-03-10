#!/usr/bin/env python3
## assaultbot - a Twitter bot that tweets words from a dictionary with optional prefix and postfix pre/ap-pended.
## LICENSE: WTFPL
## theodric 20180310 rev1
## Thanks as always to the Python docs, StackExchange, red wine, the Oxford Comma, and my cat.

import tweepy
import time
import sys
from pathlib import Path

print("\nUsage: " + str(sys.argv[0]) + " <dictionary file>\n")

argFile = str(sys.argv[1]) # loads the contents of the file passed as an argument to the script from the CLI as variable "argfile"

##############################################################################
## CONFIGURABLE ITEMS
## Hardcode your Twitter app key details here
## Create at https://apps.twitter.com/
## (Replace the filler, but leave the quotes.)

CONSUMER_KEY = 'unmodified'
CONSUMER_SECRET = 'unmodified'
ACCESS_KEY = 'unmodified'
ACCESS_SECRET = 'unmodified'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

## Set prefix and postfix for twot words (used in for loop at bottom)
prefix = "PREFIX"
postfix = "POSTFIX"

## Set frequency of tweets posted, in SECONDS
## Don't set this too low, or you may get rate-limited, or even put in Twitter Jail!
tweetFrequency = 5

## Sanity check.
if ACCESS_SECRET == 'unmodified':
    print("\nYou must first edit the script and configure a few well-labeled variables before you can use it.\n")
    exit()

##############################################################################
## OK, let's roll.

## index.txt tracks our progress through the dictionary file.
## It should be stored on persistent media (so not in /tmp),
## and gets one write per iteration. N.B. for extremely write-limited disks!

## Below, we check to see if index.txt exists at the given path.
## (Edit the path, if necessary, to suit your installation!)
## If it exists, we open it and set the value of our index variable to its contents.
## If it does not exist, we create the file, then initialize it at 0.
## N.B. you can also [create and] edit this file manually in order to set a given start value.

indexCheck = Path("./index.txt")

if indexCheck.is_file():
    indexDOTtxt='./index.txt'
    indexFile = open(indexDOTtxt, 'r')
    index = int(indexFile.read())
    indexFile.close()
else:
    print("Creating index.txt and initializing to 0...\n")
    indexDOTtxt = './index.txt'
    indexFile = open(indexDOTtxt, 'w')
    indexFile.write("0")
    indexFile.close()
    indexFile = open(indexDOTtxt, 'r')
    index = int(indexFile.read())
    indexFile.close()

## Open the text file containing our dictionary.
## We are taking the argument from the command line,
## but you can also hardcode your file here by following
## the above procedure for index.txt
wordFile = open(argFile, 'r')
words = wordFile.readlines()
wordFile.close()

##############################################################################
## Here we go.
## For each line in the words file, until we run out of lines, do some things:
for line in words:
    
    ## Print the word at the current index, make it UPPER CASE, and chomp() the trailing newline off of it.
    ## Remove the .upper method if that's not what you want
    api.update_status(prefix + str.upper(words[index].rstrip("\r\n")) + postfix)
    print("\n" + prefix + str.upper(words[index].rstrip("\r\n")) + postfix) 

    ## Increment the index value, and then write it out to disk so we keep state through restarts.
    index = index + 1
    indexFile = open(indexDOTtxt, 'w')
    indexFile.write(str(index))
    indexFile.close()
    print("\nNext twot word will be " + str.upper(words[index]))
    
    ## You may find this countdown annoying.
    ## If so, comment it out, and uncomment the last line instead.
    for i in range(tweetFrequency, 0, -1):
        time.sleep(1)
        sys.stdout.write(str((i - 1))+' ')
        sys.stdout.flush()
    #time.sleep(tweetFrequency)

