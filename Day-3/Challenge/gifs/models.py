from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 30, unique = True)

    def __str__(self):
        return self.name


class Gif(models.Model):
    title = models.CharField(max_length = 100)
    url = models.URLField()
    uploader_name = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}" 