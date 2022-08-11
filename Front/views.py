from django.shortcuts import render

def home(request):    
    return render(request , 'pages/home.html' , locals())

def inner(request):
    return render(request , 'pages/inner-page.html', locals())