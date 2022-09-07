from django.db import models

class Movie(models.Model):
    title = models.CharField(primary_key=True, max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='apptaller2/images/')
    url = models.URLField(blank = True)