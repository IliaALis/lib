from django.contrib import admin

from .models import Catalog
from .models import Author
from .models import Book



admin.site.register(Catalog)
admin.site.register(Author)
admin.site.register(Book)