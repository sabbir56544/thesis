from django.db import models
from frontpage.models import About, DonationProcess, DonorRegister, GalleryPhoto
from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets


class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = '__all__'

        widgets = {
            'discription': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput()
        }



class GalleryForm(ModelForm):
    class Meta:
        model = GalleryPhoto
        fields = '__all__'

        widgets = {
            'photos': forms.FileInput(attrs={'class': 'form-control'}), 
        }


class DonateProcessForm(ModelForm):
    class Meta:
        model = DonationProcess
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(),
            'discription': forms.Textarea(attrs={'class': 'form-control'}),
        }



