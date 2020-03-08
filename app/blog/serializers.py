from rest_framework import serializers
from .models import Blog, Comment, Course, Coursedetail


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CoursedetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coursedetail
        fields = "__all__"
