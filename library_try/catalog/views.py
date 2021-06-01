from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
	return render(request, 'catalog/index.html')


def author(request):
	return render(request, 'catalog/author.html')


def books(request):
	return render(request, 'catalog/books.html')

