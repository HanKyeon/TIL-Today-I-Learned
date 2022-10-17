from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    # path('<int:comment_pk>/comments/delete/', views.comments_delete, name='comments_delete'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:article_pk>/like/', views.like, name='like'),
    path('articles_info/', views.articles_info),
    path('articles_detail/<int:article_pk>/', views.articles_detail),
    path('comments_info/', views.comments_info),
    path('comments_detail/<int:comment_pk>/', views.comments_detail),
    # path('articles_comments/<int:article_pk>/comments/', views.articles_comments),
]
