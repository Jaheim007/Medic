from django.shortcuts import render , redirect
from django.views.generic import View
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
            print(user)
            if user is not None:
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
        
    
class Update(View):   
    template_name = 'pages/user_profile.html'
    
    def get(self , request):
        form  = forms.UpdateProfile
        return render(request , self.template_name , locals())
    
    def post(self, request):
        pass
    
        





