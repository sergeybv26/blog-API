from rest_framework import serializers

from blog_api.models import BlogPost, Comments


class CommentsSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = ['comment']

    def get_comment(self, obj):
        return obj.get_last_comment()


class CommentForPostSerializer(serializers.ModelSerializer):
    level = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'text', 'user', 'parent', 'level', 'post_id']


class PostsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'text', 'comments']

    def get_comments(self, obj):
        return obj.get_first_comment()

