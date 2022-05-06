from django.urls import path
<<<<<<< HEAD
from .views import *

urlpatterns = [
    path('', MainpageView.as_view(), name='mainpage'),
    path('aboutChan/', AboutpageView.as_view(), name='aboutpage'),
    path('contactChan/', ContactpageView.as_view(), name='contactpage'),
=======

from .views import *
urlpatterns = [
    path('', MainpageView.as_view(), name='mainpage'),
>>>>>>> 4dceddee5016159518f7fcf4efe6afecd4ad1d72
]