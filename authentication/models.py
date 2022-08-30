
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField

from Front.models import RepeatFields

class User(AbstractUser , RepeatFields): 
    MALE = "male"
    FEMALE = "female"
    
    Gender = [
        (MALE , "male"),
        (FEMALE , "female")
    ]
     
    phone = PhoneNumberField(region="CI")
    gender = models.CharField(max_length=150 , choices=Gender)
    image = models.ImageField(upload_to="User__Images" , default =" default.jpg ")
    occupation = models.CharField(max_length=150)
    

