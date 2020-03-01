from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='default')
    content = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['created']
