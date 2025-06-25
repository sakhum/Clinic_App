from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    identity_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='', blank=True, null=True)
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class MedicalNote(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Message(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender_name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    
class Notice(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    show_to_users = models.BooleanField(default=True)
    


    def __str__(self):
        return self.name

