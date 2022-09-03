"""Medicio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path , include


from authentication import views
from Front import views as front
from Hospital import views as host

urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup" ,views.Signup.as_view() , name='signup'),
    path("login" , views.Login.as_view() , name='login'),
    path("user" , views.User_profile.as_view(), name="user"),
    path("logout" , views.Logout.as_view(), name="logout"), 
    path('', front.Home.as_view(), name="home"),
    path('about', front.About.as_view(), name="about"),
    path('contact', front.Contact.as_view(), name="contact"),
    path("contact_verification", front.contact_verification , name="contact_verification"),
    path("newsletter_verification", front.newsletter_verification , name="newsletter_verification"),
    path('services', host.Services.as_view(), name="services"),
    path('department', host.Departments.as_view(), name="department"),
    path('doctors', host.Doctors.as_view(), name="doctor"), 
    path('update' , views.UpdateProfile.as_view(), name='update'),
    path('appointment' , views.Makeappointment.as_view() , name="appointment"),
    path("appointment_form" , host.appointment_form , name ="appointment_form")
    
     

]

if settings.DEBUG:   
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)