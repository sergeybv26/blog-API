from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from blog_api.models import BlogPost, Comments
from blog_api.serializers import CommentForPostSerializer, PostsSerializer, CommentsSerializer


class PostView(ListCreateAPIView):
    """Осуществляет вывод всех постов и комментариев к ним до 3 уровня вложенности"""
    queryset = BlogPost.objects.all()
    serializer_class = PostsSerializer


class SinglePostView(RetrieveUpdateDestroyAPIView):
    """Осуществляет вывод одного поста и комментариев до 3 уровня вложенности для редактирования или удаления"""
    queryset = BlogPost.objects.all()
    serializer_class = PostsSerializer


class CommentView(ListCreateAPIView):
    """Осуществляет вывод всех комментариев"""
    queryset = Comments.objects.all()
    serializer_class = CommentForPostSerializer


class SingleCommentView(RetrieveUpdateDestroyAPIView):
    """Осуществляет вывод одного комментария для его редактирования или удаления"""
    queryset = Comments.objects.all()
    serializer_class = CommentForPostSerializer


class CommentLastView(RetrieveUpdateDestroyAPIView):
    """Осуществляет вывод всех комментариев к коментарию 3 уровня"""
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
