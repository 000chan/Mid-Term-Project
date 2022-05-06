<<<<<<< HEAD
from re import template
from django.views.generic.base import TemplateView

class MainpageView(TemplateView):
    template_name = 'theme/main.html'

class AboutpageView(TemplateView):
    template_name = 'theme/main_about.html'

class ContactpageView(TemplateView):
    template_name = 'theme/main_contact.html'
=======
from django.views.generic.base import TemplateView

class MainpageView(TemplateView):
    template_name = 'theme/main.html'
>>>>>>> 4dceddee5016159518f7fcf4efe6afecd4ad1d72
