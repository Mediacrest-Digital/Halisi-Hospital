from django.urls import path
from . views import *

app_name = 'website'

urlpatterns = [
    path( "", Home, name="home", ),
    path( "about", About, name="about", ),
    path( "services", Services, name="services", ),
    path( "service/<str:pk>", ServiceView, name="service", ),
    path( "clinics", ClinicsView, name="clinics", ),
    path( "contact", Contact, name="contact", ),

    path( "careers", CareersView, name="careers", ),
    path( "career/<str:pk>", CareerView, name="career", ),
    path( "gallery", GalleryView, name="gallery", ),
]


