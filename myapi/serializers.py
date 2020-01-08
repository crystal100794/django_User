from django.contrib.auth.models import User
from rest_framework import serializers


from . import models


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('user_id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    tag = serializers.SlugRelatedField(many=True, read_only=True, slug_field='tag_name')
    posted_by = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = models.Book
        fields = ('id', 'author', 'book_name', 'description',
                  'released_date', 'tag', 'posted_by',
                  'posted_date', 'price')
        read_only_fields = ('book_name',)


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Basket
        fields = ('items', 'user', 'date_created')
        read_only_fields = ('item',)



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ('items', 'items_quality', 'date_created')
        read_only_fields = ('items', 'items_quality')

