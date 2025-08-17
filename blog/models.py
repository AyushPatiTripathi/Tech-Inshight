from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
import math 

class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True ,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/',blank=True,null =True )
    tags = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def reading_time(self):
        words = self.content.split()
        word_count = len(words)
        minutes = math.ceil(word_count / 200)
        return minutes
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = sulgify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
        
        
