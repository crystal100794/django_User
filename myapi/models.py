from django.contrib.auth.models import User
from django.db import models


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

    def __str__(self):
        return self.book_name


class Basket(models.Model):
    user = models.OneToOneField(User, related_name="user_cart", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Book)


class Order(models.Model):
    cart = models.ForeignKey(Basket, blank=True, null=True, on_delete=models.CASCADE)
    items = models.ForeignKey(Book, blank=True, null=True, on_delete=models.CASCADE)
    items_quality = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, related_name="user_item", on_delete=models.CASCADE)
