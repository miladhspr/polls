from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'names': ['milad']}
    return render(request, 'pages/landing.html',context , content_type='text/html; charset=UTF-8')

