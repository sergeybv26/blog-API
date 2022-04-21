from django.shortcuts import render

from blog_api.models import BlogPost, Comments


def index(request):
    post = BlogPost(title='1', text='qwerty')
    post.save()
    print(post.pk)
    comment1 = Comments(post_id=post, text='kjsdhfakj', user='user7')
    comment1.save()
    comment2 = Comments(post_id=post, parent=comment1, text='kjsdhfakj', user='user8')
    comment2.save()
    comment3 = Comments(post_id=post, parent=comment2, text='kjsdhfakj', user='user9')
    comment3.save()

    comment4 = Comments(post_id=post, parent=comment3, text='kjsdhfakj', user='user10')
    comment4.save()
    comment5 = Comments(post_id=post, parent=comment2, text='kjsdhfakj', user='user22')
    comment5.save()

    queryset = BlogPost.objects.all().prefetch_related('comments')

    for post in queryset:
        comments = [comm for comm in post.comments.all().order_by('parent')]
        for comm in comments:
            print(comm.user)
            print(f'Parent: {comm.parent.user}') if comm.parent else print(comm.parent)
