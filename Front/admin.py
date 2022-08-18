from django.contrib import admin
from .models import About_Us , About_Stats , About_provide , Appointment , Banner , Contact , Emergency_banner , Departments , Doctors , Services , Services_banner , SiteInfo , Testimonials , Newsletter

@admin.register(About_Us)

class About_Us(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "deleted",

    )

@admin.register(About_Stats)

class About_Stats(admin.ModelAdmin):
    list_display = (
        "title",
        "number_stats",
        "icon"
    )

@admin.register(About_provide)

class About_provide(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "icon"
    )

@admin.register(Appointment)

class Appointment(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "department",
        "appointment_date",
        "doctor",
        "message"
    )

@admin.register(Banner)

class Banner(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "image"
    )

@admin.register(Contact)

class Contact(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "message"
    )

@admin.register(Emergency_banner)

class Emergency_banner(admin.ModelAdmin):
    list_display = (
        "title",
        "description"
    )

@admin.register(Departments)

class Departments(admin.ModelAdmin):
    list_display = (
        "name",
        "description"
    )

@admin.register(Doctors)

class Doctors(admin.ModelAdmin):
    list_display = (
        "name",
        "occupation",
        "image",
        "facebook",
        "twitter",
        "instagram",
        "linkedin"
    )

@admin.register(Services)

class Services(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "icon"
    )

@admin.register(Services_banner)

class Services_banner(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "icon"
    )

@admin.register(SiteInfo)

class SiteInfo(admin.ModelAdmin):
    list_display = (
        "about_title",
        "address",
        "appointment_title",
        "contact_title",
        "copyright",
        "departments_title",
        "doctors_title",
        "opening_days",
        "services_title",
        "testimonials_title",
        "email_1",
        "email_2",
        "phone_1",
        "phone_2",
        "facebook",
        "twitter",
        "instagram",
        "linkedin"  
    )

@admin.register(Testimonials)

class Testimonials(admin.ModelAdmin):
    list_display = (
        "name", 
        "occupation", 
        "comment"    
    )

@admin.register(Newsletter)

class Newsletter(admin.ModelAdmin):
    list_display = (
        "email", 
    )