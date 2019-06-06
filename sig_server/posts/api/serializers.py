from rest_framework import serializers
from posts.models import Post, Comment
from sigs.views import get_user_detail


class PostDetailSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        user_detail = get_user_detail(obj.author_id)
        return user_detail['username']

    def get_comments(self, obj):
        queryset = Comment.objects.filter(post=obj)
        return CommentDetailSerializer(queryset, many=True).data

    class Meta:
        fields = ('id', 'content', 'created_at', 'updated_at', 'comments', 'sig', 'author_id', 'author_name')
        model = Post


class CommentDetailSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        user_detail = get_user_detail(obj.author_id)
        return user_detail['username']

    class Meta:
        fields = ('id', 'author_id', 'content', 'created_at', 'post', 'author_name')
        model = Comment
