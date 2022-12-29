from rest_framework.viewsets import ModelViewSet
from AppRestFramework.models import Post
from AppRestFramework.api.serializers import PostSerializer
import requests
import time
from rest_framework import status
from rest_framework.response import Response


class PostApiViewSet(ModelViewSet):
    serializer_class  = PostSerializer
    queryset = Post.objects.all()
    


    