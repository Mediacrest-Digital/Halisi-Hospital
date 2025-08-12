from django.shortcuts import render


from .models import Service, ClinicDay, Career, Clinic, Package, Partner, Testimonial

# Create your views here.


def Home(request):  
    services = Service.objects.all()
    days = ClinicDay.objects.all()
    partners = Partner.objects.all()
    testimonials = Testimonial.objects.all()
    homeservices = Service.objects.all()[:4]

    context = {
        "services": services,
        "days": days,
        "partners": partners,
        "testimonials": testimonials,
        "homeservices": homeservices,
    }

    return render(request, 'website/index.html', context)



def About(request):  

    services = Service.objects.all()

    context = {
        "services": services
    }

    return render(request, 'website/about_us.html', context)


def Services(request):  

    services = Service.objects.all()

    context = {
        "services": services
    }

    return render(request, 'website/services.html', context)


def ServiceView(request, *args, **kwargs):  

    service = Service.objects.get(id=kwargs['pk'])
    services = Service.objects.all()
    packages = Package.objects.all()

    context = {
        "service": service,
        "services": services,
        "packages": packages,
    }

    return render(request, 'website/service.html', context)


def ClinicsView(request):

    services = Service.objects.all()
    clinics = Clinic.objects.all()
    days = ClinicDay.objects.all()

    context = {
        "services": services,
        "clinics": clinics,
        "days": days,
    }

    return render(request, 'website/clinics.html', context)


def Contact(request):

    services = Service.objects.all()

    context = {
        "services": services
    }

    return render(request, 'website/contact_us.html', context)



def CareersView(request):

    services = Service.objects.all()
    careers = Career.objects.all()

    context = {
        "services": services,
        "careers": careers
    }

    return render(request, 'website/careers.html', context)


def CareerView(request, *args, **kwargs):  

    services = Service.objects.all()
    career = Career.objects.get(id=kwargs["pk"])

    context = {
        "career": career,
        "services": services,
    }

    return render(request, 'website/service.html', context)

def GalleryView(request):

    services = Service.objects.all()

    context = {
        "services": services
    }

    return render(request, 'website/gallery.html', context)






