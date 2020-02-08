from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as authviews
from rest_framework_jwt.views import obtain_jwt_token

from blog import views

router = DefaultRouter()
router.register(r'blog', views.BlogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    url(r'^login/', obtain_jwt_token),  # jwt login
]
