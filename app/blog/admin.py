from django.contrib import admin

from .models import Blog
from django.contrib import admin

# Register your models here.
admin.site.register(Blog)  # 注册blog到admin站点
