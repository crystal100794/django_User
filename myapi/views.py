from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from django.contrib.auth.models import User
from django.db.models import Sum
from rest_auth.registration.views import SocialLoginView
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from . import models
from . import serializers


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


# @api_view(['POST'])
# @permission_classes((AllowAny,))
# def user_create(request):
#     if request.method == 'POST':
#         serializer = serializers.UserSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response("Error", status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @permission_classes((AllowAny,))
# @csrf_exempt
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({"error" : "Missed username or password"},
#                         status=status.HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid username or password'},
#                         status=status.HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=status.HTTP_200_OK)


@api_view(['POST'])
def user_password_change(request):
    if request.method == 'POST':
        user_query = User.objects.get(pk=request.user.pk)
        serializer = serializers.UserSerializer(user_query, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response("Error", status=status.HTTP_400_BAD_REQUEST)


@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def create_book(request):
    if request.method == 'POST':
        serializer = serializers.BookSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response("Error", status=status.HTTP_400_BAD_REQUEST)


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def get_book_list(request):
    if request.method == 'GET':
        try:
            book_query = models.Book.objects.all().order_by('-posted_date')
        except models.Book.DoesNotExist:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.BookSerializer(book_query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response("Error", status=status.HTTP_400_BAD_REQUEST)


# @permission_classes([permissions.IsAuthenticated])
# @api_view(['GET'])
# def get_book_price(request):
#     if request.method == 'GET':
#         try:
#             book_query = models.Book.objects.aggregate(Sum('price'))
#         except models.Book.DoesNotExist:
#             return Response("Error", status=status.HTTP_400_BAD_REQUEST)
#
#         serializer = serializers.BookSerializer(book_query, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     return Response("Error", status=status.HTTP_400_BAD_REQUEST)


@permission_classes([permissions.IsAuthenticated])
@api_view(['DELETE'])
def delete_book(request, book_id):
    if request.method == 'DELETE':
        try:
            book_query = models.Book.objects.get(pk=book_id)
        except models.Book.DoesNotExist:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)
        if request.user == book_query.posted_by:
            book_query.delete(user=request.user)
        return Response(status=status.HTTP_200_OK)

    return Response("Error", status=status.HTTP_400_BAD_REQUEST)


@permission_classes([permissions.IsAuthenticated])
@api_view(['PUT'])
def update_book(request, book_id):
    if request.method == 'PUT':
        try:
            book_query = models.Book.objects.get(pk=book_id)
            # serializer = serializers.BookSerializer(book_query, data=request.data)
        except models.Book.DoesNotExist:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.BookSerializer(book_query, data=request.data, partial=True)

        if serializer.is_valid():
            if request.user == book_query.posted_by:
                serializer.save(user=request.user)
        return Response(status=status.HTTP_200_OK)

    return Response("Error", status=status.HTTP_400_BAD_REQUEST)


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def get_user_book(request, user_id):
    if request.method == 'GET':
        try:
            book_query = models.Book.objects.get(pk=user_id)
        except models.Book.DoesNotExist:
            return Response("Error1", status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.BookSerializer(book_query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response("Error2", status=status.HTTP_400_BAD_REQUEST)


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def get_user_profile(request, user_id):
    if request.method == 'GET':
        try:
            profile_query = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.UserSerializer(profile_query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response("Error", status=status.HTTP_400_BAD_REQUEST)


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET', 'POST'])
def get_basket(request):
    if request.method == 'GET':
        try:
            cart_query = models.Basket.objects.get(user=request.user)
        except models.Basket.DoesNotExist:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.BasketSerializer(cart_query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        try:
            cart_query = models.Basket.objects.get(user=request.user)
        except models.Book.DoesNotExist:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.BasketSerializer(cart_query, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(user=request.user)
        return Response(status=status.HTTP_200_OK)

    return Response("Error", status=status.HTTP_400_BAD_REQUEST)


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET', 'POST'])
def get_item(request):
    if request.method == 'GET':
        try:
            cart_query = models.Order.objects.get(user=request.user)
        except models.Order.DoesNotExist:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.OrderSerializer(cart_query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        try:
            item_query = models.Order.objects.get(user=request.user)
        except models.Book.DoesNotExist:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.OrderSerializer(item_query, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(user=request.user)
        return Response(status=status.HTTP_200_OK)

    return Response("Error", status=status.HTTP_400_BAD_REQUEST)
