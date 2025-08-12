from django.contrib import admin

from .models import Service, Clinic, Career, ClinicDay, Package, Partner, Testimonial
# Register your models here.

admin.site.register(Career)
admin.site.register(Clinic)
admin.site.register(ClinicDay)
admin.site.register(Service)
admin.site.register(Package)
admin.site.register(Partner)
admin.site.register(Testimonial)
