from django.db import models

# Create your models here.

'''У додатку blog, створіть модель Post з полями 
title (CharField), 
content (TextField), 
та published_date (DateTimeField).

За бажанням ви можете додати власні поля. '''

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    published_date = models.DateField()