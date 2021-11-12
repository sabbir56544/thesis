from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import DonorRegister
    
    
class DonorRegistration(ModelForm):
    class Meta:
        model = DonorRegister
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'gender' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'date_of_birth' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
            'blood_group' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'phone_number' : forms.TextInput(attrs={'class':'form-control', 'required':'True', 'placeholder': '+880********'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'required':'True'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'student_id': forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'address' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'any_diseases' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'bleeding_disorders' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
          
            
        }
        


class DonorSearch(forms.Form):
    blood_group_s_choice = (
        ("empty" , "Select blood group"),
        ("a+" , "A+"),
        ("a-" , "A-"),
        ("b+" , "B+"),
        ("b-" , "B-"),
        ("o+" , "O+"),
        ("o-" , "O-"),
        ("ab+" , "AB+"),
        ("ab-" , "AB-"),
    )

    
    blood_group = forms.ChoiceField(
        choices=blood_group_s_choice,
        widget=forms.Select(
            attrs={'class':'form-control',
            'required':'True',
            },
            ),
    )


    near_hospital_choices=[
        ("empty" , "Select Hospital"),
        ("Khulna City Medical","Khulna City Medical"),
        ("Khulna Medical College Hospital","Khulna Medical College Hospital"),
        ("Khulna Sadar Hospital", "Khulna Sadar Hospital"),
        ("Islami Bank Hospital", "Islami Bank Hospital"),
        ("SANDHANI Hospital KHULNA", "SANDHANI Hospital KHULNA"),
        ("Khulna Healthcare Hospital", "Khulna Healthcare Hospital"),
        ("Surokkha Hospital & Diagnostic", "Surokkha Hospital & Diagnostic"),
        ('Addin Hospital', 'Addin Hospital'),

    ]

    near_hospital = forms.ChoiceField(
        choices=near_hospital_choices,
        widget=forms.Select(
            attrs={'class':'form-control',
            'required':'True',
            },
            ),
    )
    

   

