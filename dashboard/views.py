from django.shortcuts import render, redirect
from frontpage.models import About, DonationProcess, DonorRegister, GalleryPhoto
from .forms import AboutForm, DonateProcessForm, GalleryForm
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, admin_only
from django.utils.decorators import method_decorator
from django.views.generic import DetailView


@allowed_users(allowed_roles=['admin'])
@login_required
@admin_only
def dashboard_view(request):
    try:    
        total_donor = DonorRegister.objects.all()
        total_donors = total_donor.count()

        now = datetime.now() # current date and time
        hour = now.strftime("%H")# current hour
        hour = int(hour)

        donors = DonorRegister.objects.all().filter(blood_group='A+')
        a_donor = donors.count()

        donors = DonorRegister.objects.all().filter(blood_group='A-')
        a_negative_donor = donors.count()

        donors = DonorRegister.objects.all().filter(blood_group='B+')
        b_donor = donors.count()

        donors = DonorRegister.objects.all().filter(blood_group='B-')
        b_negative_donor = donors.count()

        donors = DonorRegister.objects.all().filter(blood_group='O+')
        o_donor = donors.count()

        donors = DonorRegister.objects.all().filter(blood_group='O-')
        o_negative_donor = donors.count()
        

        donors = DonorRegister.objects.all().filter(blood_group='AB+')
        ab_donor = donors.count()

        donors = DonorRegister.objects.all().filter(blood_group='AB-')
        ab_negative_donor = donors.count()

        context = {
            'total_donor': total_donors,
            'hour': hour,
            'total_a_donor': a_donor,
            'total_a_negative_donor': a_negative_donor,
            'total_b_donor':b_donor,
            'total_b_negative_donor': b_negative_donor,
            'total_o_donor': o_donor,
            'total_o_negative_donor': b_negative_donor,
            'total_ab_donor': ab_donor,
            'total_ab_negative_donor': ab_negative_donor,
        }
        return render(request, 'dashboard/index.html', context)

    except:
        return render(request, "errors404.html")   


@login_required
@admin_only
def search_donor(request):
    try:
        if request.method == 'POST':
            search_keyword = request.POST['search_keyword']
            serach_items = DonorRegister.objects.filter(blood_group__contains=search_keyword)
            return render(request, 'dashboard/search.html', {'serach_items': serach_items, 'serch_key': search_keyword})
        return render(request, 'dashboard/search.html')
    except:
        return render(request, "errors404.html")


@login_required
@admin_only
def about_view(request):
    form = AboutForm()
    if request.method == "POST":
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'product was successfully added')
            return redirect('dashboard')

    context = {
        'form': form,
    }
    return render(request, 'dashboard/about_form.html', context)


@login_required
@admin_only
def donate_photo_view(request):
    form = GalleryForm()
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Images Has Been Uploaded')
            return redirect('dashboard')

    context = {
        'form': form,
    }        

    return render(request, 'dashboard/about_form.html', context)


@login_required
@admin_only
def donate_process(request):
    form = DonateProcessForm()
    if request.method == "POST":
        form = DonateProcessForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Images Has Been Uploaded')
            return redirect('dashboard')

    context = {
        'form': form,
    }        

    return render(request, 'dashboard/about_form.html', context)

@login_required
@admin_only
def donor_list(request):
    donors = DonorRegister.objects.all()
    context = {
        'donor_list': donors,
    }  
    return render(request, 'dashboard/donor_list.html', context)


@login_required
@admin_only
def donor_detail(request, pk):
    donor = DonorRegister.objects.get(pk=pk)
    context = {
        'donors': donor,
    }

    return render(request, 'dashboard/donor_detail.html', context)


