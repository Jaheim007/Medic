from Front.views import home , inner 
from django.urls import path

urlpatterns = [
    path('' , home , name='home') , 
    path('inner/' , inner , name='inner'), 
]
 