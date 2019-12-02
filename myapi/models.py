from django.contrib.auth.models import User
from django.db import models


# class Author(models.Model):
#     username        = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.username
#
# class Poster(models.Model):
#     username        = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.username

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class BookTag(models.Model):
    tag_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.tag_name


class Book(models.Model):
    author = models.ManyToManyField(Person)
    book_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(null=True, blank=True)
    book_content = models.TextField(blank=True)
    released_date = models.DateTimeField(blank=True, null=True)
    tag = models.ManyToManyField(BookTag)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True, blank=True)


    # class Meta:
    #     unique_together = ('book_name',)

    def __str__(self):
        return self.book_name

