from django.contrib import admin
from .models import About, GalleryPhoto, DonationProcess, DonorRegister, Hospital


admin.site.register(About)
admin.site.register(GalleryPhoto)
admin.site.register(DonationProcess)
admin.site.register(Hospital)

class DonorRegisterAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'phone_number', 'today_date']
admin.site.register(DonorRegister, DonorRegisterAdmin)



