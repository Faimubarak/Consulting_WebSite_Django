from django.db import models

# Create your models here.

class AboutUs(models.Model):
    location = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    email = models.EmailField()