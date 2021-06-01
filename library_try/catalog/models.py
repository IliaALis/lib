from django.db import models


class Catalog(models.Model):
	author_name = models.CharField('author_name', max_length=50)
	author_books = models.TextField('books written')	

	def __str__(self):
		return self.author_name, self.author_books




class Author(models.Model):
	author_name = models.CharField('author_name', max_length=50)
	author_books = models.TextField('books written')
	about_author = models.TextField('about author')

	def __str__(self):
		return self.author_name, self.author_books, self.about_author



class Book(models.Model):
	author = models.ForeignKey(Author, on_delete =models.CASCADE)
	book_name = models.CharField('book_name', max_length=50)
	author_name = models.CharField('author_name', max_length=50)
	book_description = models.TextField('books description')

	def __str__(self):
		return self.author, self.book_name, self.author_name, self.book_description

