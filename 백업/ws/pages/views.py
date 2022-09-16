from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dinner(request, menu, num):
    context = {'menus':menu, 'num':num}
    return render(request, 'dinner.html', context)