from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from authentication.models import User

from Front import models 

class Home(View):
    template_name = 'pages/home.html'
    
    def get(self , request): 
        banners = models.Banner.objects.all() 
        emergencies = models.Emergency_banner.objects.first()
        services = models.Services.objects.all()
        return render(request , self.template_name , locals())
    
    def post(self, request):
        pass

class About(View):
    template_name = 'pages/about.html'
    
    def get(self , request):
        about = models.About_Us.objects.first()
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class Services(View):
    template_name = 'pages/services.html'
    
    def get(self , request):
        services = models.Services.objects.all()
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class Contact(View):
    template_name = 'pages/contact.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        msg =''
        success = True
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")
        
        contact = models.Contact(
            name = name, 
            email = email, 
            subject = subject, 
            message = message
        )
        
        contact.save()
        msg = 'Un message a été envoyé à votre adresse e-mail'
    
        data = {
        'msg': msg,
        'success': success
        }

        return JsonResponse(data, safe=False)
    
class Departments(View):
    template_name = 'pages/departments.html'
    
    def get(self , request):
        departments = models.Departments.objects.all() 
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class Doctors(View):
    template_name = 'pages/doctors.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class Appointmnet(View):
    template_name = 'pages/appointments.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass

class User_profile(View):
    template_name = 'pages/user_profile.html'
    
    def get(self , request):
        users = User.objects.filter()
        return render(request , self.template_name , locals())
    
    def post(self, request):
        pass
    






