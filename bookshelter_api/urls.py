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

from django.contrib.auth.decorators import login_required
from django.urls import path
from api.views import UserRegistrationView, UserLoginView, UserLogoutView, UserProfileView, BookListView, BookDetailView, csrf_token_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/csrf_token/', csrf_token_view, name='csrf_token_view'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('addbook/', login_required(BookListView.as_view()), name='add_book'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<int:pk>/edit/', login_required(BookDetailView.as_view()), name='edit_book'),
    path('books/<int:pk>/delete/', login_required(BookDetailView.as_view()), name='delete_book'),
    path('profile/', login_required(UserProfileView.as_view()), name='profile'),
    # path('favorites/', FavoritesView.as_view(), name='favorites'),
    # path('cart/', CartView.as_view(), name='cart')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)