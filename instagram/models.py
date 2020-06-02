from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user_name = models.CharField(max_length =30)
    bio = models.CharField(max_length =30)
    email = models.EmailField()
    
    def __str__(self):
        return self.user_name
    class Meta:
        ordering = ['user_name']
        
        
    def save_profile(self):
        self.save()
        
   
class Post(models.Model):
    caption = models.CharField(max_length =30)
    like = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to = 'post/')
    
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return instagram

    def __str__(self):
        return self.caption
    
class Following(models.Model):
    username = models.CharField(blank=True,max_length = 255)
    followed = models.CharField(blank=True,max_length = 255)


