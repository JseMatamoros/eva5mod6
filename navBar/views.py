from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'index.html')

def navbar(request):
    return render(request, 'navbar.html')