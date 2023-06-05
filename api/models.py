from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set', blank=True)
    account_type = models.CharField(max_length=10, choices=(('admin', 'Admin'), ('user', 'User')), default='user')

    def is_admin(self):
        return self.account_type == 'admin'

class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cover_photo=models.ImageField(upload_to='covers/')

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    rating = models.IntegerField(choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
