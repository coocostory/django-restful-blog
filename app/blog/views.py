from django.shortcuts import render

from rest_framework import viewsets
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .others.blogpagenation import BlogPagination as BasicPagination

from .others.permission import Public


# from rest_framework.authentication import TokenAuthentication
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    pagination_class = BasicPagination
    authentication_classes = [TokenAuthentication]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    pagination_class = BasicPagination
    permission_classes = (Public,)


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
