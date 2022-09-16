"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')), 
    path('pages/', include('pages.urls'))
]





'''
원래 urls

from django.contrib import admin
from django.urls import path
from articles import views
from pages import views as page_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('dinner/', views.dinner), 
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('fake-google/', views.fake_google),
    path('hello/<str:name>/', views.hello),

    path('pages-index/', page_views.index),
]
'''