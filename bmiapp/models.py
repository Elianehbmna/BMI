from django.db import models

from django.contrib.auth.models import User
# Create your models here.
import datetime as dt
from tinymce.models import HTMLField


class Profile(models.Model):
    bio=models.TextField(max_length=100,blank=True,default="bio please...")
    profilepic=models.ImageField(upload_to='profile/', blank = True,default='../static/images/bad-profile-pic-2.jpeg')
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user

class Result(models.Model):
    
    weight = models.FloatField(blank=True,default=0)
    height = models.FloatField(blank=True,default=0)
    BMI = models.FloatField(blank=True,default=0)
    result = models.TextField( blank=True,null=True)
    user_profile=models.ForeignKey(Profile)
    user=models.ForeignKey(User)

    
    
    
    def __str__(self):
       return self.weight
