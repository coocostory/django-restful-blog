from django.shortcuts import render

from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# from rest_framework.authentication import TokenAuthentication
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    from .others.blogpagenation import BlogPagination
    pagination_class = BlogPagination
    authentication_classes = [TokenAuthentication]


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
