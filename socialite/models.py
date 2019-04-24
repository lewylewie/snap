from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Profile(models.Model):
    image_cover = models.FileField()
    image_caption = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('socialite:index')

class Comment(models.Model):
    image_cover = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField()

    def get_absolute_url(self):
        return reverse('socialite:index')

