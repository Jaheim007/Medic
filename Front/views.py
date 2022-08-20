from django.shortcuts import render

def home(request):    
    return render(request , 'pages/home.html' , locals())

def about(request):    
    return render(request , "pages/about.html" , locals())
