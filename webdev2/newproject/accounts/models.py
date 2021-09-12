from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import requests
import os
from urllib.parse import urljoin
from django.utils import timezone



# Create your models here.
class Profile(models.Model):
    user =                      models.OneToOneField(User, on_delete=models.CASCADE)
    followernumber =            models.IntegerField(blank = True, null = True)
    date_updated =              models.DateTimeField(auto_now=True)
    title =                     models.CharField(max_length=100, null = True)
    def __str__(self):
            return str(self.title)

class Repository(models.Model):
    repname =                   models.CharField(max_length=100, default='', null=True, blank = True)
    starrating =                models.IntegerField(default=0, null = True, blank = True)
    owner =                     models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.repname
    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Repositories"


def create_repository(sender, **kwargs):
    if kwargs['created']:
        str = urljoin('https://api.github.com/users/',kwargs['instance'].title+'/')
        responserepo = requests.get(urljoin(str,'repos'))
        drepo = responserepo.json()
        for i in range(len(drepo)):
            rep = Repository.objects.create(owner = kwargs['instance'], repname=drepo[i]['name'], starrating = drepo[i]['stargazers_count'])

def create_profile(sender, **kwargs):
    if kwargs['created']:
        response = requests.get(urljoin('https://api.github.com/users/',kwargs['instance'].username))
        d = response.json()
        user_profile = Profile.objects.create(user=kwargs['instance'], followernumber = int(d['followers']), title = kwargs['instance'].username)
        user_profile.save()

        
post_save.connect(create_profile, sender=User)
post_save.connect(create_repository, sender = Profile)

