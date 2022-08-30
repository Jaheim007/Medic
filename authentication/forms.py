from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

from .models import User

class NewUserForm(UserCreationForm):    
    email = forms.EmailField(required=True)
    
    class Meta:   
        model = User
        fields = ("first_name" , "last_name", "username", "email", "password1", "password2")
        
class LoginForm(forms.Form):      
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    
class UpdateProfile(ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["first_name" , "last_name", "username", "email", "password" ,"image" , "gender", "occupation", "phone" ]
            
    
    