from django.contrib import admin
from .models import Book, Person, BookTag, Basket_item


# admin.site.register(Author)
admin.site.register(Person)
admin.site.register(Book)
admin.site.register(BookTag)
admin.site.register(Basket_item)
