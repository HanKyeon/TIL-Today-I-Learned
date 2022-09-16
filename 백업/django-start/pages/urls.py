from django.urls import path, include
from pages import views


app_name = "pages"
urlpatterns = [
    path('index/', views.index, name="index"), 
    # path('articles/', include('articles.urls'))
]
