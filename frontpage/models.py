from django.contrib.auth.models import User
from django.db import models



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

    near_hospital_choices=[
        ("Khulna City Medical","Khulna City Medical"),
        ("Khulna Medical College Hospital","Khulna Medical College Hospital"),
        ("Khulna Sadar Hospital", "Khulna Sadar Hospital"),
        ("Islami Bank Hospital", "Islami Bank Hospital"),
        ("SANDHANI DONOR CLUB KHULNA", "SANDHANI DONOR CLUB KHULNA"),
        ("Khulna Healthcare Hospital", "Khulna Healthcare Hospital"),
        ("Surokkha Hospital & Diagnostic", "Surokkha Hospital & Diagnostic"),

    ]

    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=gender_choices)
    date_of_birth = models.CharField(max_length=40)
    blood_group = models.CharField(max_length=4, choices=blood_choices)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    occupation = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    last_donate_date = models.CharField(max_length=50)
    any_diseases = models.CharField(max_length=4, choices=any_diseases_choices)
    bleeding_disorders = models.CharField(max_length=4, choices=bleeding_disorders_choices)
    near_hospital = models.CharField(max_length=100, choices=near_hospital_choices, default="Khulna Medical College Hospital")
    today_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    

    def __str__(self):
        return self.name


