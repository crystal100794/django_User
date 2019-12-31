from django.contrib import admin
from . import models


# admin.site.register(Author)
admin.site.register(models.Person)
admin.site.register(models.Book)
admin.site.register(models.BookTag)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)
