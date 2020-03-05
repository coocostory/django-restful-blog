from django.contrib import admin

from .models import Blog, Comment, Coursedetail, Course
from django.contrib import admin

# Register your models here.
admin.site.register(Blog)  # 注册blog到admin站点
admin.site.register(Comment)
admin.site.register(Coursedetail)
admin.site.register(Course)
