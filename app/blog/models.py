from django.db import models


# Create your models here.
class Blog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='default')
    content = models.TextField()

    class Meta:
        ordering = ['created']
