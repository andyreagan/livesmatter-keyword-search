# processTweets.py
# crawl the tweets, and look for keywords
# output with daily resolution
#
# NOTES
# uses the new 15-minute compressed format
# 
# USAGE 
# gzip -cd tweets.gz | python processTweet.py 2014-01-01 keywords
#  
# this will read keywords.txt and the tweets from stdin
# and save a frequency file, labMT vector in keywords/[keyword]
# for each keyword

# we'll use most of these
from json import loads,dumps
import codecs
import datetime
import re
import sys

def tweetreader(tweet,outfile):
    # takes in the hashtag-stripped text
    # the keyword list
    # and the title of the file to append to
    for keyword in keywords:
        if keyword["re"].search(tweet["text"]) is not None:
            # print("match for {0}:".format(keyword["folder"]))
            # print(tweet["text"])
            g = codecs.open("raw-tweets/{0}/{1}.txt".format(keyword["folder"],outfile),"a","utf8")
            g.write(dumps(tweet))
            g.write("\n")
            g.close()
        # else:
            # print("no match for {0}".format(keyword["folder"]))

def gzipper(outfile):
    f = sys.stdin
    for line in f:
        try:
            tweet = loads(line)
        except:
            print "failed to load a tweet"
        if "text" in tweet:
            # print("found text")
            tweetreader(tweet,outfile)

keywords = [{"re": re.compile(r"#blacklivesmatter\b",flags=re.IGNORECASE), "folder": "blacklivesmatter",},
            {"re": re.compile(r"#alllivesmatter\b",flags=re.IGNORECASE), "folder": "alllivesmatter",},
            {"re": re.compile(r"#bluelivesmatter\b",flags=re.IGNORECASE), "folder": "bluelivesmatter",},
            {"re": re.compile(r"#policelivesmatter\b",flags=re.IGNORECASE), "folder": "policelivesmatter",},
            {"re": re.compile(r"#michaelbrown\b",flags=re.IGNORECASE), "folder": "michaelbrown",},
            {"re": re.compile(r"#ferguson\b",flags=re.IGNORECASE), "folder": "ferguson",},
            {"re": re.compile(r"#freddiegray\b",flags=re.IGNORECASE), "folder": "freddiegray",},
            {"re": re.compile(r"#ericgarner\b",flags=re.IGNORECASE), "folder": "ericgarner",},
            {"re": re.compile(r"#icantbreathe\b",flags=re.IGNORECASE), "folder": "icantbreathe",},
            {"re": re.compile(r"#sarahbland\b",flags=re.IGNORECASE), "folder": "sarahbland",},
            {"re": re.compile(r"#templeton\b",flags=re.IGNORECASE), "folder": "templeton",},]

def makefolders():
    from os import mkdir
    for a in keywords:
        mkdir("raw-tweets/"+a["folder"])

if __name__ == "__main__":
    # load the things
    outfile = sys.argv[1]

    gzipper(outfile)
    
    print("complete")

    # makefolders()

  








