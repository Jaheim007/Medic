from Front.views import home , about , services , departments , doctor , contact, appointment




from django.urls import path

urlpatterns = [
    path('' , home , name='home'), 
    path('about', about , name='about'),
    path('services', services , name='services'),
    path('contact', contact , name='contact'),
    path('department', departments , name='department'),
    path('doctor', doctor , name='doctor'),
    path('appointment' , appointment, name= "appointment"),
]
 