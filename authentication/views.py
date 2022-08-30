from django.shortcuts import render , redirect
from django.views.generic import View
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout

from authentication import forms

from authentication.models import User


class Signup(View):  
    template_name = 'pages/signup.html'
    
    def get(self , request):
        form  = forms.NewUserForm
        return render(request , self.template_name , locals())
    
    def post(self , request): 
        if request.method == "POST": 
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
               
            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username, 
                email = email, 
                password = password1,  
            )
            
            user.save()
            
            send_mail(
                "Bienvenue à Medicio",
                "Votre adresse e-mail a été vérifiée",
                'jaheimkouaho@gmail.com',
                [email],
                fail_silently=False
            )
            
            login(request, user)
            
            return redirect("/login")
        
        return render(request , self.template_name , locals())  
        
        
class Login(View):  
    template_name = 'pages/login.html'
    
    def get(self , request):    
        form = forms.LoginForm
        return render(request , self.template_name , locals())
    
    def post(self , request): 
        form = forms.LoginForm(request.POST)
        if form.is_valid():     
            user = authenticate(
                username=form.cleaned_data["username"], 
                password=form.cleaned_data["password"]
            )
            
            if user:
                login(request, user)
                return redirect("/") 
            else:     
                print("User not Found") 
    
        return render(request , self.template_name , locals())
    
class Logout(View):
    
    def get(self , request):
        logout(request)
        return redirect("/login")
        
    def post(self, request):
        pass
        
class User_profile(View):
    template_name = 'pages/user_profile.html'
    
    def get(self , request):
        users = User.objects.filter()
        return render(request , self.template_name , locals())
    
    def post(self, request):
        if request.method == "POST": 
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            image = request.POST.get("image")
            phone = request.POST.get("phone")
            occupation = request.POST.get("occupation")
            gender = request.POST.get("gender")
            
            
            user = User.objects.all(
                first_name = first_name,
                last_name = last_name,
                username = username, 
                email = email, 
                password = password,
                gender = gender, 
                image = image , 
                phone = phone, 
                occupation = occupation
                 
            )
            
            user.save()
            
            login(request, user)
            
            return redirect("/login")
        
        return render(request , self.template_name , locals())  
    
class UpdateProfile(View):
    template_name =  'pages/edit.html' 
    class_form = forms.UpdateProfile
    
    def get(self , request):
        form = self.class_form(instance=request.user)
        
        return render(request , self.template_name , locals())
            
    
    def post(self, request):
        form = self.class_form(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect("update")
        return redirect("update")
        
            
        
         
    

        
    
        





