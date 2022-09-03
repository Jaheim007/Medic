from django.shortcuts import render
from Hospital import models
from django.views.generic import View
from django.http import JsonResponse
from django.core.mail import send_mail
   
class Departments(View):
    template_name = 'pages/departments.html'
    
    def get(self , request):
        departments = models.Departments.objects.all() 
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class Doctors(View):
    template_name = 'pages/doctors.html'
    
    def get(self , request):
        doctors = models.Doctors.objects.all()
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    

    
def appointment_form(request): 
       msg =''
       success = True
       if request.method == "POST":
           name = request.POST.get("name")
           email = request.POST.get("email")
           doctor = request.POST.get("doctor")
           appointment_date = request.POST.get("appointment_date")
        
       appointment = models.Appointment(
           name = name,
           email = email,
           doctor = doctor, 
           appointment_date = appointment_date,  
       )
        
       appointment.save()
       msg = 'You have successfully made an appointment , a message has been sent to your email.'

       send_mail(
                "Your Appoinment Request",
                "You have successfully made an appointment, we will contact you via your phone in a few days. ",
                'jaheimkouaho@gmail.com',
                [email],
                fail_silently=False
        )
       data = {
        'msg': msg,
        'success': success
        }
        
       return JsonResponse(data, safe=False) 
    


    
class Services(View):
    template_name = 'pages/services.html'
    
    def get(self , request):
        services = models.Services.objects.all()
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass