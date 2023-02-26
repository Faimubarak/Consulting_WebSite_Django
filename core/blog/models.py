from django.db import models
from consulat.models import Catgory
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_post')
    title = models.CharField(max_length=100)
    content = models.TextField()
    catgory = models.ForeignKey(Catgory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title