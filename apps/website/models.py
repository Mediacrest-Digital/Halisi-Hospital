from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.


class Service(models.Model):

    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="services")
    excerpt = models.TextField()
    description = HTMLField()

    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name


class ClinicDay(models.Model):
    days = (
        ( 'Sunday', 'Sunday', ),
        ( 'Monday', 'Monday', ),
        ( 'Tuesday', 'Tuesday', ),
        ( 'Wednesday', 'Wednesday', ),
        ( 'Thursday', 'Thursday', ),
        ( 'Friday', 'Friday', ),
        ( 'Saturday', 'Saturday', ),
       
    )
    day = models.CharField(max_length=20, null=True, choices=days)
    image = models.ImageField(upload_to="clinics")


    def __str__(self):
        return self.day


class Clinic(models.Model):

    times = (
        ( '8:00am', '8:00am', ),
        ( '9:00am', '9:00am', ),
        ( '10:00am', '10:00am', ),
        ( '11:00am', '11:00am', ),
        ( '12:00pm', '12:00pm', ),
        ( '1:00pm', '1:00pm', ),
        ( '2:00pm', '2:00pm', ),
        ( '3:00pm', '3:00pm', ),
        ( '4:00pm', '4:00pm', ),
        ( '5:00pm', '5:00pm', ),
        ( '6:00pm', '6:00pm', ),
    )

    
    name = models.CharField(max_length=255, null=True)
    day = models.ForeignKey(ClinicDay, on_delete=models.CASCADE, null=True)
    start = models.CharField(max_length=20, null=True, choices=times)
    end = models.CharField(max_length=20, null=True, choices=times)
    
    date_created = models.DateTimeField(default=timezone.now)


    @property
    def allDay(self):
        return self.day.day

    def __str__(self):
        return self.name
    


class Package(models.Model):

    name = models.CharField(max_length=255, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    downloader = models.FileField(upload_to="products", null=True)
    
    @property
    def relatedService(self):
        return self.service.name

    def __str__(self):
        return self.name


class Testimonial(models.Model):

    image = models.ImageField(upload_to="testimonials")


    def __str__(self):
        return str(self.id)
    

class Partner(models.Model):

    name = models.CharField(max_length=255, null=True)
    logo = models.ImageField(upload_to="partners")

    def __str__(self):
        return str(self.name)



class Career(models.Model):

    status_list = (
        ( 'Active', 'Active', ),
        ( 'Not Active', 'Not Active', ),
    )

    name = models.CharField(max_length=255, null=True)
    requirements = HTMLField()
    summary = HTMLField()
    status = models.CharField(max_length=20, choices=status_list)

    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)
