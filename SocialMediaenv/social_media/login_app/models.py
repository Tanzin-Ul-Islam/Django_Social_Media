from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profilepic = models.ImageField(upload_to = 'userpics', blank=True)
    coverpic =  models.ImageField(upload_to = 'coverpics', blank=True)
    description = models.TextField(blank=True)
    full_name = models.CharField(max_length=200, blank=True)
    dob = models.DateField(blank=True, null = True)
    website = models.URLField(blank = True)
    facebook = models.URLField(blank=True)

class follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followings')
    created_date = models.DateTimeField(auto_now_add=True)

