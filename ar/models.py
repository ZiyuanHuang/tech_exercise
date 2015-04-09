from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateTimeField(
            'date published')
    category = models.CharField(max_length=200)
    text = models.TextField()
    preview_text = models.TextField()
    def __str__(self):
        return self.title
    
