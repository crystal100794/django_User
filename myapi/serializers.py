from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    tag = serializers.SlugRelatedField(many=True, read_only=True, slug_field='tag_name')
    posted_by = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = models.Book
        fields = ('author', 'book_name', 'description', 'released_date', 'tag', 'posted_by', 'posted_date')