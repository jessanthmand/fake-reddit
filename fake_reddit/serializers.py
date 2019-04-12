from rest_framework import serializers
from .models import Comments, Posts

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('created_at', 'content', 'preview_url',)

class PostsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    class Meta:
        model = Posts
        fields = ('created_at', 'title', 'picture_url', 'content', 'site_url', 'vote_total',)