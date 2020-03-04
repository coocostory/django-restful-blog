from django.shortcuts import render

from rest_framework import viewsets, mixins
from .models import Blog, Comment, Course, Coursedetail, User
from .serializers import BlogSerializer, CommentSerializer, CoursedetailSerializer, CourseSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .others.blogpagenation import BlogPagination as BasicPagination

from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated


# from rest_framework.authentication import TokenAuthentication
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    pagination_class = BasicPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    pagination_class = BasicPagination
    permission_classes = [AllowAny]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class CoursedetailViewSet(viewsets.ModelViewSet):
    queryset = Coursedetail.objects.all()
    serializer_class = CoursedetailSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CustomToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk
        })
