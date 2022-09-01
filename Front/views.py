from django.shortcuts import render , redirect
from django.views.generic import View
from django.http import JsonResponse
from django.core.mail import send_mail

from authentication.models import User

from Front import models 

from Hospital import models as host

class Home(View):
    template_name = 'pages/home.html'
    
    def get(self , request): 
        banners = models.Banner.objects.all() 
        emergencies = models.Emergency_banner.objects.first()
        services = host.Services.objects.all()
        return render(request , self.template_name , locals())
    
    def post(self, request):
        pass

class About(View):
    template_name = 'pages/about.html'
    
    def get(self , request):
        about = models.About_Us.objects.first()
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass

    
class Contact(View):
    template_name = 'pages/contact.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
def contact_verification(request):
        msg =''
        success = True
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")
        
        contact = models.Contact(
            name = name, 
            email = email, 
            subject = subject, 
            message = message
        )
        
        contact.save()
        msg = 'Thank you for contacting Medicio.'
        
        send_mail(
                "Bienvenue à Medicio",
                "Thank you for contacting Medicio we will contact you via your phone in a few days. ",
                'jaheimkouaho@gmail.com',
                [email],
                fail_silently=False
        )
    
        data = {
        'msg': msg,
        'success': success
        }

        return JsonResponse(data, safe=False)
    
def newsletter_verification(request):
        msg =''
        success = True
        if request.method == "POST":
            email = request.POST.get("email")

        
        newsletter = models.Newsletter(
            email = email
        )
        
        newsletter.save()
        msg = 'Thank you for contacting Medicio'
        
        send_mail(
                "Bienvenue à Medicio",
                "Thank you for contacting Medicio we will contact you via your phone in a few days. ",
                'jaheimkouaho@gmail.com',
                [email],
                fail_silently=False
        )
    
        data = {
        'msg': msg,
        'success': success
        }

        return JsonResponse(data, safe=False)
    
 
        
    


    
    






