from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
#def home(request):
#    return render(request, 'home.html')

class IndexView(TemplateView):
    template_name = "patternfly/home.html"

class LoginView(TemplateView):
    template_name = "patternfly/login.html"