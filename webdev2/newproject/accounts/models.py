from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user =                      models.OneToOneField(User, on_delete=models.CASCADE)
    followernumber =            models.IntegerField(default=0)
    lastupdate =                models.DateTimeField(blank = True, null = True)
    title = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title


class Repository(models.Model):
    owner =                     models.ForeignKey(Profile, on_delete=models.CASCADE)
    repname =                   models.CharField(max_length=100, default='')
    starrating =                models.IntegerField(default=0)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'], title=kwargs['instance'])

post_save.connect(create_profile, sender=User)        
