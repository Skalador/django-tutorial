from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class IndexView(TemplateView):
    template_name = "htmlcsstemps/index.html"

#def index(request):
#    template = loader.get_template("htmlcsstemps/index.html")
#    return HttpResponse(template.render(request))