from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book, Library

def home(request):
    return HttpResponse("Welcome to the Library App!")

def books_list(request):
    books = Book.objects.all()
    output = ", ".join([book.title for book in books])
    return HttpResponse(f"Books: {output}")

def library_detail(request, id):
    library = get_object_or_404(Library, pk=id)
    return HttpResponse(f"Library: {library.name}, Location: {library.location}")
