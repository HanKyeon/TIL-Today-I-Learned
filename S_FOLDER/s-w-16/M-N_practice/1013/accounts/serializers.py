from rest_framework import serializers
from .models import User
# from articles.models import Article, Comment
from articles.serializers import ArticleListSerializer, CommentSerializer

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('followings',)

class SubUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        ead_only_fields = ('followings',)

class UserSerializer(serializers.ModelSerializer):
    write_articles = ArticleListSerializer(many=True, read_only=True)
    like_articles = ArticleListSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    followings = SubUserSerializer(many=True, read_only=True)
    followers = SubUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'