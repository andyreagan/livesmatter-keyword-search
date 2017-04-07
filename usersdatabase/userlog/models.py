from django.db import models

# Create your models here.
class Tweeter(models.Model):
    submitted_date = models.DateTimeField(null=True, blank=True)
    submitted = models.BooleanField(default=False)
    username = models.CharField(max_length=100)
    userid = models.IntegerField()
    numtweetsfound = models.IntegerField(default=0)



