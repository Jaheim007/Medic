from django.shortcuts import render
from Hospital import models
from django.views.generic import View
from django.http import JsonResponse
   
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
    
class Appointmnet(View):
    template_name = 'pages/appointments.html'
    
    def get(self , request):
        doctors = models.Doctors.objects.all()
        return render(request , self.template_name , locals())
    
    def post(self , request): 
        msg =''
        success = True
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            department = request.POST.get("department")
            doctor = request.POST.get("doctor")
            appointment_date = request.POST.get("appointment_date")
        
        appointment = models.Appointment(
            name = name,
            email = email,
            department = department, 
            doctor = doctor, 
            appointment_date = appointment_date,  
        )
        
        appointment.save()
        
        msg = 'Un message a été envoyé à votre adresse e-mail'

        data = {
            'msg': msg,
            'success': success
        }
        
        
        return JsonResponse(data, safe=False)   
    
def appointment_form(request): 
    msg = ''
    success = True 
    if request.method == "POST":   
        name = request.POST.get("name")
        email = request.POST.get("email")
        department = request.POST.get("department")
        doctor = request.POST.get("doctor")
        appointment_date = request.POST.get("appointment_date")
        
        
    appointment_form = models.Appointment(
        name = name , 
        email = email ,
        department = department , 
        doctor = doctor , 
        appointment_date = appointment_date
    )
    
    appointment_form.save()
    
    msg = 'Bonjour'
    
    data ={
        "msg" : msg , 
        "success" : success
    } 
    
    return JsonResponse(data , safe = False)

    
class Services(View):
    template_name = 'pages/services.html'
    
    def get(self , request):
        services = models.Services.objects.all()
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass