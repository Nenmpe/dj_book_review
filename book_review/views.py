from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def book_detail(request, bid):
    # book = Book.objects.get(id=bid) # might throw error if the data does not exists in the db
    book = Book.objects.filter(id=bid).first  # Will send empty queryset instead of throwing error if the data does not exists in the db
    # '.first' ends first instance of object instead of whole queryset
    return render(request, 'book_detail.html', {'book':book})

