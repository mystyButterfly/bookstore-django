from django.shortcuts import render
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def cart(request):
    id = request.GET.get('id')
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        book = None
    return render(request, 'cart.html', {'book': book})

def about(request):
    return render(request, 'about.html')
