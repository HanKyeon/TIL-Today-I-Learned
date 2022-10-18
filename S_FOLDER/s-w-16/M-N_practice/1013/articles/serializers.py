from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'user')

class ArticleUserCount(serializers.ModelSerializer):
    
    class Meta:
        pass

class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    writer_followers = serializers.SerializerMethodField(method_name='wirters_followers')

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_users')

    def writers_followers(self, obj):
        return self



