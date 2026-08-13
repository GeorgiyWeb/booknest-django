from django.shortcuts import render
from django.utils import timezone
from .models import Book

# Create your views here.


def home(request):
    context = {
        'message' : "Welcome to BookNest — Bookstore Management System!",
        'today' : timezone.now().date()
    }
    return render(request, 'home.html', context)


def dashboard(request):
    items = Book.objects.all()
    
    context = {
        'items' : items
    }
    
    return render(request, 'catalog/dashboard.html', context)