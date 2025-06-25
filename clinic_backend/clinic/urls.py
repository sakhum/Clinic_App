from django.urls import path
from .views import patient_list, delete_patient, patient_form_view, update_patient
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('patients/', patient_list),  # GET & POST
    path('patients/<int:patient_id>/', delete_patient),  # DELETE
    path('patients/<int:patient_id>/edit/', update_patient),  # ✅ NEW: PUT for updating
    path('form/', patient_form_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

