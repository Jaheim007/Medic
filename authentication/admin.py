from django.contrib import admin
from .models import User

@admin.register(User)

class User(admin.ModelAdmin):   
    list_display = (
        "username",
        "first_name", 
        "last_name", 
        "email", 
        "phone",
        "date_of_birth",
        "gender",
        "photo"
    )
