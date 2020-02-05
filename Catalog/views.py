from django.shortcuts import render
from Catalog.models import Book, Author, BookInstance, Genre
from django.http import HttpResponse

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(
	    status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors, }

    ren = render (request, 'index.html', context = context)
    return ren
    #render(request, template_name, context=None, content_type=None, status=None, using=None)