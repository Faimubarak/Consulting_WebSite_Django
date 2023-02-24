from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Counslat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    publish_date = models.DateField(default=timezone.now)
    description = models.TextField(max_length =1000)
    catgoray = models.ForeignKey('Catgory', on_delete=models.SET_NULL , null = True, blank = True)

    def __str__(self):
        return self.name





class Catgory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    created_at = models.DateField(default=timezone.now)
    counslat = models.ForeignKey(Counslat, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)