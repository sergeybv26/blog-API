from django.shortcuts import render

from blog_api.models import BlogPost, Comments


def index(request):
    post = BlogPost(title='1', text='qwerty')
    post.save()
    print(post.pk)
    comment1 = Comments(post_id=post, text='kjsdhfakj', user='user1')
    comment1.save()
    comment2 = Comments(post_id=post, parent=comment1, text='kjsdhfakj', user='user2')
    comment2.save()

    queryset = BlogPost.objects.all().prefetch_related('comments')

    for post in queryset:
        comments = [comm for comm in post.comments.all()]
        for comm in comments:
            print(comm.user)
            print(comm.parent)
