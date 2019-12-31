from django.contrib.auth.models import User
from django.db import models

from django_User import settings


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class BookTag(models.Model):
    tag_name = models.CharField(unique=True, max_length=100, blank=True)

    def __str__(self):
        return self.tag_name


class Book(models.Model):
    author = models.ManyToManyField(Person)
    book_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(null=True, blank=True)
    book_content = models.TextField(blank=True)
    released_date = models.DateTimeField(blank=True, null=True)
    tag = models.ManyToManyField(BookTag)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
    posted_date = models.DateTimeField(auto_now_add=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quality = models.IntegerField()

    def __str__(self):
        return self.book_name


class Cart(models.Model):
    user = models.OneToOneField(User, related_name="user_cart", on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, blank=True, null=True, on_delete=models.CASCADE)
    items = models.OneToOneField(Book, blank=True, null=True, on_delete=models.CASCADE)
    items_quality = models.IntegerField(default=1, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
