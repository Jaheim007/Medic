from django.shortcuts import render

def home(request):    
    return render(request , 'pages/home.html' , locals())

def about(request):    
    return render(request , "pages/about.html" , locals())

def services(request):   
    return render(request , "pages/services.html" , locals())

def departments(request):    
    return render(request , 'pages/departments.html' , locals())

def appointment(request):    
    return render(request , 'pages/appointments.html' , locals())

def contact(request):    
    return render(request , 'pages/contact.html' , locals())

def doctor(request):    
    return render(request , 'pages/doctors.html' , locals())


