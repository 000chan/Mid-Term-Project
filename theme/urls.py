from django.urls import path
from .views import *

urlpatterns = [
    path('', MainpageView.as_view(), name='mainpage'),
    path('aboutChan/', AboutpageView.as_view(), name='aboutpage'),
    path('contactChan/', ContactpageView.as_view(), name='contactpage'),
]