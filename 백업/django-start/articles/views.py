from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    print("=====================here===================")
    print("HI HELLO", request)
    print("=====================here===================")
    # return HttpResponse("<h1>hola</h1>")
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ['apple', 'orange', 'banana']
    info = {"name" : "HanKyeon"}
    context = {
        'food' : foods, 
        'info' : info, 
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['초밥', '치킨', '빠에야', '라구 파스타']
    pick = random.choice(foods)
    context = {
        'foods' : foods, 
        'pick' : pick
    }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    data = request.GET.get('message') # input의 name과일치해야함.
    context = {'data':data}
    return render(request, 'articles/catch.html', context)

def fake_google(request):
    return render(request, 'articles/fake-google.html')

def hello(request, name): # 여기 name은 urls.py에서 받은 변수 <str:name>이다.
    context = {'name': name}
    return render(request, 'articles/hello.html', context)
