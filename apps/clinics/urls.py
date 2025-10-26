from django.urls import path
from . import views

urlpatterns = [
    path('', views.docs_view, name='docs'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:patient_id>/update/', views.update_patient, name='update_patient'),
    path('patients/<int:patient_id>/delete/', views.delete_patient, name='delete_patient'),
    path('form/', views.patient_form_view, name='patient_form'),
]
