from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class RepeatFields(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

class Departments(RepeatFields):
    
    class Meta: 
        verbose_name = "Department"
        verbose_name_plural = "Departments"  
    
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField( upload_to="Departments__Images")


    def __str__(self):
        return self.name
   

class Doctors(RepeatFields):
    
    class Meta: 
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors" 
         
    name  = models.CharField(max_length=150)
    image = models.ImageField(upload_to="Doctors__Images")
    department = models.ManyToManyField(Departments, related_name="doctor_department")
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()

    
    def __str__(self):
        return self.name
    
    
class Appointment(RepeatFields):
    
    class Meta: 
        verbose_name = "Appointment"
        verbose_name_plural = "Appointment" 
        
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    department = models.CharField(max_length=150)
    appointment_date = models.DateField()
    doctor = models.CharField(max_length=150)
    
    
    def __str__(self):
        return self.name
    
class Services(RepeatFields):
    
    class Meta: 
        verbose_name = "Services"
        verbose_name_plural = "Services" 

    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title
    
   
