from django.contrib import admin
from django.urls import path, include
from apps.clinics.views import docs_view, patient_form_view, patient_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', docs_view),
    path('patients/', patient_list),
    path('form/', patient_form_view),
    path('admin/', admin.site.urls),
    path('api/', include('apps.clinics.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
