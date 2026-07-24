from django.shortcuts import render
from .models import Page


def home(request):
    page = Page.objects.filter(slug='home').first()
    return render(request, 'core/home.html', {'page': page})


def about(request):
    return render(request, 'core/about.html', {})