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

urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup" ,views.Signup.as_view() , name='signup'),
    path("login" , views.Login.as_view() , name='login'),
    path("user" , front.User_profile.as_view(), name="user"),
    path("logout" , views.Logout.as_view(), name="logout"), 
    path('', front.Home.as_view(), name="home"),
    path('about', front.About.as_view(), name="about"),
    path('services', front.Services.as_view(), name="services"),
    path('department', front.Departments.as_view(), name="department"),
    path('appointment', front.Appointmnet.as_view(), name="appointment"),
    path('contact', front.Contact.as_view(), name="contact"),
    path('doctors', front.Doctors.as_view(), name="doctor")
]

if settings.DEBUG:   
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)