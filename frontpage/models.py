from django.contrib.auth.models import User
from django.db import models

from django.core.exceptions import ValidationError

class About(models.Model):
    discription = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return str(self.image)



class GalleryPhoto(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    photos = models.ImageField()

    def __str__(self):
        return str(self.pk)

        
class DonationProcess(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    discription = models.TextField()

    def __str__(self):
        return self.title


class DonorRegister(models.Model):

    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    blood_choices=[
        ("A+" , "A+"),
        ("A-" , "A-"),
        ("B+" , "B+"),
        ("B-" , "B-"),
        ("O+" , "O+"),
        ("O-" , "O-"),
        ("AB+" , "AB+"),
        ("AB-" , "AB-"),

    ]

    any_diseases_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]

    bleeding_disorders_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]


    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=gender_choices)
    date_of_birth = models.CharField(max_length=40)
    blood_group = models.CharField(max_length=4, choices=blood_choices)
    phone_number = models.CharField(max_length=14, default="+880")
    email = models.EmailField()
    occupation = models.CharField(max_length=50)
    student_id = models.CharField(max_length=25, blank=True, null=True)
    address = models.CharField(max_length=50)
    any_diseases = models.CharField(max_length=4, choices=any_diseases_choices)
    bleeding_disorders = models.CharField(max_length=4, choices=bleeding_disorders_choices)
    today_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    

    def __str__(self):
        return self.name

