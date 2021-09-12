from django.contrib import admin
from .models import Profile, Repository
from django.db import models


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','followernumber', 'date_updated', 'title')

class RepositoryAdmin(admin.ModelAdmin):
    list_display = ('repname','owner', 'starrating')



admin.site.register(Profile,ProfileAdmin)
admin.site.register(Repository, RepositoryAdmin)
