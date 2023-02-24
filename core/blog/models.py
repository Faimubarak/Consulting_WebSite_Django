from django.db import models
from consulat.models import Catgory
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    catgory = models.ForeignKey(Catgory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title