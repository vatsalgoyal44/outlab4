from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user =                      models.OneToOneField(User, on_delete=models.CASCADE)
    first_name =                models.CharField(('first name'), max_length=30, blank=False)
    followernumber =            models.IntegerField(default=0)
    lastupdate =                models.DateTimeField(blank = True)

class Repository(models.Model):
    owner =                     models.ForeignKey(Profile, on_delete=models.CASCADE)
    repname =                   models.CharField(max_length=100, default='')
    starrating =                models.IntegerField(default=0)