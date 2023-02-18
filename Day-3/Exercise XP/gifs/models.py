from django.db import models


# Create your models here.
class Gif(models.Model):
    title = models.CharField(max_length=100, null=True)
    url = models.URLField()
    uploader_name = models.CharField(max_length=120, null=True)
    created_at = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    gifs = models.ManyToManyField(Gif, related_name='categories', blank=True)
    
    def __str__(self):
        return self.name