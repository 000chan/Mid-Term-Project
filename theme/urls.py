from django.urls import path
from .views import *
from django.views.generic import RedirectView

urlpatterns = [
    path('', MainpageView.as_view(), name='mainpage'),
    path('aboutChan/', AboutpageView.as_view(), name='aboutpage'),
    path('aboutChan/aboutChan', RedirectView.as_view(url="/home/aboutChan/")),
    path('aboutChan/contactChan', RedirectView.as_view(url="/home/contactChan/")),
    path('contactChan/', ContactpageView.as_view(), name='contactpage'),
    path('contactChan/', RedirectView.as_view(url="/contactChan/")),
    path('contactChan/contactChan', RedirectView.as_view(url="/home/contactChan/")),
    path('contactChan/aboutChan', RedirectView.as_view(url="/home/aboutChan/")),
]