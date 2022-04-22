from django.urls import path

from blog_api.views import PostView, SinglePostView, CommentView, CommentLastView

app_name = 'blog_api'

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>', SinglePostView.as_view()),
    path('comments', CommentView.as_view()),
    path('last_comment/<int:pk>', CommentLastView.as_view())
]
