from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import is_valid_path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from articles import serializers
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # 400리턴
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 201 리턴
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 400리턴

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) # 삭제하고 나면 204가 정확한 응답이다.
    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data) # article_list의 POST와 다른 점은 data가 첫번째 인자가 아니고 인스턴스가 첫째 인자라서 data를 위에서는 명시해줘야 한다.
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) # 그냥 수정 200이라서 status에 대해 별도 입력 안해도 된다.

@api_view(['GET'])
def comment_list(request):
    if request.method == "GET":
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)










