from django.contrib import admin

from Hospital import models


@admin.register(models.Departments)

class Departments(admin.ModelAdmin):
    list_display = (
        "name",
        "description"
    )

@admin.register(models.Doctors)

class Doctors(admin.ModelAdmin):
    list_display = (
        "name",
        "image",
        "facebook",
        "twitter",
        "instagram",
        "linkedin"
    )

@admin.register(models.Services)

class Services(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "icon"
    )

@admin.register(models.Appointment)

class Appointment(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "department",
        "appointment_date",
        "doctor",
  
    )