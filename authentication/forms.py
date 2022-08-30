from django import forms
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
    
class UpdateProfile(UserChangeForm):
    email = forms.EmailField(required=True)
    
    class Meta:   
        model = User
        fields = ("first_name" , "last_name", "username", "email", "password1", "password2" , "phone" , "date_of_birth" , "gender", "occupation", "image" )
    
    
    