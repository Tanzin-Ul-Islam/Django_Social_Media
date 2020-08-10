from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to='postpic')
    caption = models.CharField(max_length=200, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-upload_date']

class like(models.Model):
    lpost = models.ForeignKey(post, on_delete=models.CASCADE, related_name='liked_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')

    def __str__(self):
        return str(self.user)+' liked '+str(self.lpost)

class dislike(models.Model):
    dpost = models.ForeignKey(post, on_delete=models.CASCADE, related_name='disliked_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disliker')

    def __str__(self):
        return str(self.user)+' disliked '+str(self.dpost)