from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# from django.http import HttpResponse, HttpResponseForbidden
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comments.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)

# @require_POST
# def delete(request, pk):
#     article = Article.objects.get(pk=pk)
#     if request.user.is_authenticated:
#         if request.user == article.user:
#             article.delete()
#             return redirect('articles:index')
#         return HttpResponseForbidden()
#     return HttpResponse(status=401)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)

@require_POST
def like(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        # 좋아요 취소
        # request.user in article.like_users.all() # request.user가 article.like_users에 있다면 취소.
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        # 좋아요
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')


@api_view(['GET', 'POST'])
def articles_info(request):
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
def articles_detail(request, article_pk):
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
def comments_info(request):
    if request.method == "GET":
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comments_detail(request, comment_pk):
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

# def articles_comments(request, article_pk):
#     pass





