from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from blog_api.models import BlogPost, Comments
from blog_api.serializers import CommentForPostSerializer, PostsSerializer, CommentsSerializer


class PostView(ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostsSerializer


class SinglePostView(RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostsSerializer


class CommentView(ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentForPostSerializer


class CommentLastView(RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
