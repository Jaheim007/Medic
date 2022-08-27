from django.shortcuts import render
from django.views.generic import View


from authentication.models import User
from Front import models 

class Home(View):
    template_name = 'pages/home.html'
    
    def get(self , request): 
          
        return render(request , self.template_name , locals())
    
    def post(self, request):
        pass

class About(View):
    template_name = 'pages/about.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class Services(View):
    template_name = 'pages/services.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class Contact(View):
    template_name = 'pages/contact.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
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
    






