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


class OrderSerializer(serializers.ModelSerializer):
    items = BookSerializer(read_only=True)
    items_quantity = serializers.IntegerField()
    items_price = serializers.SerializerMethodField(read_only=True)

    def get_items_price(self, obj):
        return obj.items.price * obj.items_quantity

    class Meta:
        model = models.Order
        fields = ('items', 'items_quantity', 'items_price')


class BasketSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(read_only=True, many=True)
    total_price = serializers.SerializerMethodField(read_only=True)

    def get_total_price(self,obj):
        return obj.orders.items_price

    class Meta:
        model = models.Basket
        fields = ('user', 'orders', 'total_price')
