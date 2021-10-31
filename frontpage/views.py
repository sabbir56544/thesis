from django.shortcuts import redirect, render
from .models import About, GalleryPhoto, DonationProcess, DonorRegister
from .forms import DonorRegistration, DonorSearch
from django.contrib import messages

from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def home_view(request): 
    about = About.objects.all()
    gallery = GalleryPhoto.objects.all()
    d_process = DonationProcess.objects.all()
    context = {
        'abouts': about,
        'gallery': gallery,
        'process': d_process,
        'form': 'form',
    }
    return render(request, 'index.html', context)


def register_view(request):
    form = DonorRegistration()
    if request.method == 'POST':
        form = DonorRegistration(request.POST)
        email = request.POST['email']
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank You for being part in this Blood Bank')

            mydict = {'email': email}
            html_template = 'send_email.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Welcome to Nubtk Blood Donor'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()
            return redirect('home')    
    context = {
        'form': form,
    }    

    return render(request, 'registration.html', context)


def search_view(request):
    search_forms = DonorSearch()
    if request.method == "POST":
        search_forms = DonorSearch(request.POST)
        if search_forms.is_valid():
            blood_group = search_forms.cleaned_data['blood_group']
            
            donor_filter = DonorRegister.objects.filter(blood_group__icontains=blood_group)
            
            context = {
                'donor_filter': donor_filter,
            }

            return render(request, 'donor_list.html', context)

    context = {
        'forms': search_forms,
    }     

    return render(request, 'search.html', context)   


