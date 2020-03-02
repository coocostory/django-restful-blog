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
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_user = models.CharField(max_length=100, default='匿名')
    discuss = models.CharField(max_length=256, null=False)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']


class Course(models.Model):
    name = models.CharField(max_length=36)  # 课程名
    period = models.CharField(max_length=36)  # 开课时段
    classes1 = models.CharField(max_length=36, null=False)  # 课程分类
    classes2 = models.CharField(max_length=36, null=True)
    classes3 = models.CharField(max_length=36, null=True)


class CourseDetail(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    detail = models.TextField()
