"""
URL configuration for bookshelter_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import UserRegistrationView, UserLoginView, UserLogoutView, csrf_token_view

urlpatterns = [
    path('api/csrf_token/', csrf_token_view, name='csrf_token_view'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # path('books/', BookView.as_view(), name='book_list'),
    # path('books/<int:pk>/', BookView.as_view(), name='book_detail'),
    # path('addbook/', BookView.as_view(), name='add_book'),
    # path('editbook/', BookView.as_view(), name='edit_book'),
    # path('profile/', UserProfileView.as_view(), name='profile'),
    # path('favorites/', FavoritesView.as_view(), name='favorites'),
    # path('cart/', CartView.as_view(), name='cart')
]
