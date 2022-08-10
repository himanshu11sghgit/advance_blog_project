from django.db import models

# Create your models here.



class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    date_created = models.DateField(auto_now=True)
    last_updated = models.DateField(auto_now_add=True)

