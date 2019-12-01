from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    # def change_object(self, attrs, instance=None):
    #     attrs['password'] = make_password(attrs['password'])
    #     return (UserSerializer, self).change_object\
    #                             (attrs, instance=None)