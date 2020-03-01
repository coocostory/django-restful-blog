from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
