from django.shortcuts import render

# Create your views here.
app_name = 'pages'
def index(request):
    return render(request, 'pages/index.html', name="pindex")