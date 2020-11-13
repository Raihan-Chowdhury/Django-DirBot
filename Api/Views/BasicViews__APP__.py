from django.shortcuts import render

from rest_framework import generics,permissions
from .serializers import Postserializer

from .models import Post


# Create your views here.
class ShowList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer # .serializers -> PostSerializer
        
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = Postserializer

    def perform_create(self, serializer):
        serializer.save(poster = self.request.user)
