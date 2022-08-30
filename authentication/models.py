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
    date_of_birth = models.DateField(blank=True , null=True)
    gender = models.CharField(max_length=150 , choices=Gender)
    image = models.URLField(default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')
    occupation = models.CharField(max_length=150)
    

