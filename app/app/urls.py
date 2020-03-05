from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as authviews
from rest_framework_jwt.views import obtain_jwt_token

from blog import views

# 可视化的文档
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()
router.register(r'blog', views.BlogViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'coursedetail', views.CoursedetailViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url(r'^api-token-auth/', views.CustomToken.as_view()),
    path('coursedetail/<int:courseid>', views.CoursedetailList.as_view())

    # url(r'^login/', obtain_jwt_token),  # jwt login
]

#  可视化文档
schema_view = get_swagger_view(title='API文档')
urlpatterns += [
    path(r'docs/', schema_view),
]
