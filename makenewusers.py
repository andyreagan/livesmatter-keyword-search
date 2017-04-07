import sys
import os
sys.path.append('/users/a/r/areagan/fun/twitter/keyword-searches/2015-10-livesmatter/usersdatabase')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','usersdatabase.settings')
import django
django.setup()

from userlog.models import Tweeter

# print(Tweeter.objects.all())

f = open("newusers.txt", "r")
userIDs = list(map(int,f.read().rstrip().split(",")))
f.close()

print(len(Tweeter.objects.all()))
for userID in userIDs:
    t = Tweeter(submitted=False,username="",userid=userID)
    t.save()

# print(Tweeter.objects.all())
print("total number of people:")
print(len(Tweeter.objects.all()))

print("still to go:")
remaining = Tweeter.objects.filter(submitted=False)
print(len(remaining))

