from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='default')
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    comment_user = models.CharField(max_length=100, default='匿名')
    comment = models.CharField(max_length=256, null=False)
    likes = models.IntegerField(default=0)
