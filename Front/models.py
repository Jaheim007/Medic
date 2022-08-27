from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class RepeatFields(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

class About_Us(RepeatFields): 
    
    class Meta: 
        verbose_name = "About_Us"
        verbose_name_plural = "About_Us" 

    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)
    description = models.TextField()
    description_2 = models.TextField()
    list_item_1 = models.CharField(max_length=150)
    list_item_2 = models.CharField(max_length=150)
    list_item_3 = models.CharField(max_length=150)
    image = models.URLField()
    
    def __str__(self):
        return self.title
   
class About_Stats(RepeatFields):
    
    class Meta: 
        verbose_name = "About_Stats"
        verbose_name_plural = "About_Stats" 
    
    number_stats = models.IntegerField()   
    description = models.TextField()
    icon = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    
class Appointment(RepeatFields):
    
    class Meta: 
        verbose_name = "Appointment"
        verbose_name_plural = "Appointment" 
        
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField()
    department = models.CharField(max_length=150)
    appointment_date = models.DateField()
    doctor = models.CharField(max_length=150)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Banner(RepeatFields):
    
    class Meta: 
        verbose_name = "Banner"
        verbose_name_plural = "Banner" 
     
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.URLField() 
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
     
    class Meta: 
        verbose_name = "Contact"
        verbose_name_plural = "Contact" 
       
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
   
class Departments(RepeatFields):
    
    class Meta: 
        verbose_name = "Department"
        verbose_name_plural = "Departments"  
    
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.name

class Doctors(RepeatFields):
    
    class Meta: 
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors" 
         
    name  = models.CharField(max_length=150)
    occupation = models.CharField(max_length=150) 
    image = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    
    def __str__(self):
        return self.name
    
class Emergency_banner(RepeatFields):
    
    class Meta: 
        verbose_name = "Emergency_banner"
        verbose_name_plural = "Emergency_banner" 
    
    title = models.CharField(max_length=150)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Services(RepeatFields):
    
    class Meta: 
        verbose_name = "Services"
        verbose_name_plural = "Services" 

    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title
    
class SiteInfo(RepeatFields):
    
    class Meta: 
        verbose_name = "SiteInfo"
        verbose_name_plural = "SiteInfo" 
    
    about_title = models.CharField(max_length=150)                                                    
    address = models.CharField(max_length=150)
    appointment_title = models.CharField(max_length=150)
    contact_title = models.CharField(max_length=150)
    copyright = models.CharField(max_length=150)                                                     
    departments_title = models.CharField(max_length=150) 
    doctors_title = models.CharField(max_length=150)
    opening_days = models.CharField(max_length=150)
    services_title = models.CharField(max_length=150)                                                                                                                                                                                                                                                             
    testimonials_title = models.CharField(max_length=150)                                                    
                                       
    email_1 = models.CharField(max_length=150)                                                    
    email_2 = models.CharField(max_length=150)                                                    
    phone_1 = models.CharField(max_length=150)                                                    
    phone_2 = models.CharField(max_length=150)                                                    
    
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    
    def __str__(self):
        return self.about_title
    
class Testimonials(RepeatFields):
    
    class Meta: 
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
     
    name = models.CharField(max_length=150)
    occupation = models.CharField(max_length=150)
    comment = models.TextField()
    
    def __str__(self):
        return self.name
   
class Newsletter(RepeatFields):
    
    class Meta: 
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"
        
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.email
    

    
    
    
    

    


    
