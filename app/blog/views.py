from django.shortcuts import render

from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
