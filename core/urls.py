from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Halisi Family Hospital"
admin.site.site_title = "Halisi Family Hospital"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.website.urls')),
]


urlpatterns += static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )
urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
