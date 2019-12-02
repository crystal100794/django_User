from django.contrib import admin
from .models import Book, BookTag, Person


# admin.site.register(Author)
admin.site.register(Person)
admin.site.register(Book)
admin.site.register(BookTag)