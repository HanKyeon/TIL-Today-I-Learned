from django.urls import path
from . import views


urlpatterns = [
    path('html/', views.article_html), # 여태까지 하던 방식. 페이지 전체 렌더링해서 응답. html을 응답으로 받는다.
    path('json-1/', views.article_json_1),
    path('json-2/', views.article_json_2),
    path('json-3/', views.article_json_3),
]
