import sys
import os
sys.path.append('/users/a/r/areagan/fun/twitter/keyword-searches/2015-10-livesmatter/usersdatabase')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','usersdatabase.settings')
import django
django.setup()

from userlog.models import Tweeter

# print(Tweeter.objects.all())

# f = open("usernames-lives-matter.txt", "r")
# userIDs = list(map(int,f.read().rstrip().split(",")))
# f.close()
# # print(userIDs)

# Tweeter.objects.all().delete()
# print(Tweeter.objects.all())
# for userID in userIDs:
#     t = Tweeter(submitted=False,username="",userid=userID)
#     t.save()

# print(Tweeter.objects.all())
print("total number of people:")
print(len(Tweeter.objects.all()))

print("still to go:")
remaining = Tweeter.objects.filter(submitted=False)
print(len(remaining))

from sys import argv
# import urllib2
# urllib2.disable_warnings()
import datetime
from twython import Twython, TwythonError
import json
from os.path import isfile

def stealer(twitter,user_id):
    try:
        user_info = twitter.lookup_user(user_id=user_id)[0]
    except TwythonError as e:
        print(e)
        return [{"note": "account not found", "error": repr(e)}],0
    if user_info["protected"]:
        return [{"note": "private account"}],0
    num_statuses = user_info["statuses_count"]
    api_calls = 1
    alltweets = twitter.get_user_timeline(id=user_id,count=200)
    stolen = len(alltweets)
    if num_statuses > 0:
        min_id = alltweets[-1]["id"]
    while stolen < 3100 and stolen < num_statuses and api_calls < 20:
        api_calls += 1
        tweets = twitter.get_user_timeline(id=user_id,count=200,max_id=min_id)
        alltweets.extend(tweets)
        min_id = alltweets[-1]["id"]
        stolen = len(alltweets)
    print("made {0} api calls".format(api_calls))
    return alltweets,api_calls


if __name__ == '__main__':

    # store the keys somewhere (so I can share this script)
    f = open('keys','r')
    APP_KEY = f.readline().rstrip()
    APP_SECRET = f.readline().rstrip()
    OAUTH_TOKEN = f.readline().rstrip()
    OAUTH_TOKEN_SECRET = f.readline().rstrip()
    f.close()

    if not isfile('key_oauth2'):
        print("no oauth2 auth yet, attempting to get")
        # twitter = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
        # send a tweet
        # tweet='test at {0}'.format(datetime.datetime.now().strftime('%H-%M on %Y-%m-%d'))
        # twitter.update_status(status=tweet)

        # log in to twitter and get an oauth 2 token
        twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
        ACCESS_TOKEN = twitter.obtain_access_token()
        # print(ACCESS_TOKEN)
        f = open('key_oauth2','w')
        f.write(ACCESS_TOKEN)
        f.close()
    else:
        print("using oauth2 auth")
        
    # log in as oauth 2
    # some endpoints have a higher rate limit
    # store the keys somewhere (so I can share this script)
    f = open('key_oauth2','r')
    ACCESS_TOKEN = f.readline().rstrip()
    f.close()
    app = Twython(APP_KEY, access_token=ACCESS_TOKEN)

    allowed_calls = 300
    # for testing
    allowed_calls = 200
    i = 0
    while allowed_calls > 16:
        user_id = remaining[i].userid
        # user_id = 55931868 # this is me!
        print("{0} allowed calls left, getting tweets for user {1}".format(allowed_calls,user_id))
        remaining[i].submitted = True
        remaining[i].submitted_date = datetime.datetime.now()

        tweets,calls = stealer(app,user_id)
        print(len(tweets))

        allowed_calls -= calls
        remaining[i].numtweetsfound = len(tweets)
        remaining[i].save()
    
        print("saving...")
        f = open('user-tweets/{0}.json'.format(user_id),'w')
        json.dump(tweets,f,indent=4)
        f.close()
        i+=1
