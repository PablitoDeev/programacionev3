from django.shortcuts import render
from .models import NavbarItem, AboutUs, Service

def home(request):
    navbar_items = NavbarItem.objects.all()
    return render(request, 'main/home.html', {'navbar_items': navbar_items})

def about(request):
    navbar_items = NavbarItem.objects.all()
    about_info = AboutUs.objects.first()
    return render(request, 'main/about.html', {'navbar_items': navbar_items, 'about_info': about_info})

def services(request):
    navbar_items = NavbarItem.objects.all()
    services = Service.objects.all()
    return render(request, 'main/services.html', {'navbar_items': navbar_items, 'services': services})