import os
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Patient

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_patient(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)

        # Delete the photo file if it exists
        if patient.photo and os.path.isfile(patient.photo.path):
            os.remove(patient.photo.path)

        patient.delete()
        return JsonResponse({'message': 'Patient and photo deleted'})
    except Patient.DoesNotExist:
        return JsonResponse({'error': 'Patient not found'}, status=404)

@csrf_exempt
def patient_list(request):
    if request.method == 'GET':
        patients = list(Patient.objects.values())
        return JsonResponse(patients, safe=False)

    elif request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('date_of_birth')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        identity = request.POST.get('identity_number')
        photo = request.FILES.get('photo')

        patient = Patient.objects.create(
            name=name,
            date_of_birth=dob,
            email=email,
            phone=phone,
            identity_number=identity,
            photo=photo
        )
        return JsonResponse({'message': 'Patient created successfully'})

def patient_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('date_of_birth')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        identity = request.POST.get('identity_number')
        photo = request.FILES.get('photo')

        patient = Patient(
            name=name,
            date_of_birth=dob,
            email=email,
            phone=phone,
            identity_number=identity,
            photo=photo
        )
        patient.save()
        return JsonResponse({'message': 'Patient created successfully'})
    return render(request, 'form.html')

def docs_view(request):
    return render(request, 'docs.html')

@csrf_exempt
@require_http_methods(["PUT"])
def update_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    patient.name = request.POST.get('name', patient.name)
    patient.email = request.POST.get('email', patient.email)
    patient.phone = request.POST.get('phone', patient.phone)
    patient.identity_number = request.POST.get('identity_number', patient.identity_number)
    patient.save()
    return JsonResponse({'message': 'Patient updated successfully'})
