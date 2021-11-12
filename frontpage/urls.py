from django.urls import path
from .views import home_view, register_view, search_view


urlpatterns = [
    path('', home_view, name='home'),
    path('register', register_view, name='donor-registration'),
    path('search', search_view, name='donor-search'),
    path('search/donorlist', search_view, name='donor-list'),

]



