from frontpage.views import search_view
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import about_view, dashboard_view, donate_photo_view, donate_process, donor_list, donor_detail, search_donor


urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('donor/search', search_donor, name='search-donor-dashobard'),
    path('about', about_view, name='about-view'),
    path('photos', donate_photo_view, name='photo-view'),
    path('process', donate_process, name='process-view'),
    path('donor/list', donor_list, name='donor-list'),
    path('donor/detail/<int:pk>', donor_detail, name='donor-detail'),

]
