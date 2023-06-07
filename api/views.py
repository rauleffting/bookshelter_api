from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import UserSerializer, BookSerializer, FavoriteSerializer
from api.models import Book, Favorite
from django.contrib.auth import authenticate, login, logout

from django.middleware.csrf import get_token
from django.http import JsonResponse

def csrf_token_view(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            serialized_user = UserSerializer(user).data
            return Response({'message': 'User registered succesfully.', 'user': serialized_user})
        return Response(serializer.errors, status=400)

class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful.'})
        return Response({'message': 'Invalid username or password.'}, status=401)

class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful.'})
    
class UserProfileView(APIView):    
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_superuser:
            return Response({'message': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BookDetailView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        if not request.user.is_superuser:
            return Response({'message': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        if not request.user.is_superuser:
            return Response({'message': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response({'message': 'Book deleted successfully!'}, status=204)
    
class FavoriteListView(APIView):
    def get(self, request):
        user = request.user
        favorites = Favorite.objects.filter(user=user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        book_id = request.data.get('book_id')
        book = Book.objects.get(pk=book_id)

        favorite = Favorite(user=user, book=book)
        favorite.save()
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data, status=201)
    
    def delete(self, request, pk):
        favorite = Favorite.objects.get(pk=pk)
        favorite.delete()
        return Response({'message': 'Favorite removed successfully!'}, status=204)