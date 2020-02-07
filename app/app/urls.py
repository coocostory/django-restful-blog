from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog import views

router = DefaultRouter()
router.register(r'blog', views.BlogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
