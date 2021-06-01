from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('author/', views.author, name='author'),
	path('books/', views.books, name='books'),
	


]