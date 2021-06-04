from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import AbstractUser
# class Costumer(models.Model):
#     user = models.ForeignKey(User, related_name='profile',on_delete=models.CASCADE)
#     # CID = models.IntegerField(default=1)
#     #Email = models.CharField(max_length=50)
#     #Name = models.CharField(max_length=50)
#     Num = models.IntegerField()
#     Province = models.CharField(max_length=50)
#     City = models.CharField(max_length=50)
#     # Registered = models.BooleanField()
#     address =models.TextField(max_length=250, blank=True,validators=[MaxLengthValidator(250)])
#     postal_code = models.IntegerField(default=0)

class User(AbstractUser):
    Num = models.IntegerField()
    Province = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    address =models.TextField(max_length=250,validators=[MaxLengthValidator(250)])
    postal_code = models.IntegerField()

class Author(models.Model):
    AID = models.IntegerField()
    AName = models.CharField(max_length=50)

class Category(models.Model):

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.title)


class Book(models.Model):
    def __str__(self):
        return self.name

    BID = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    summery = models.CharField(max_length=200)
    rating = models.FloatField()
    image = models.ImageField(upload_to='Images/', default='Images/None/Noimg.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Year = models.IntegerField(default=1400)
    Edition = models.IntegerField(default=1)
    Price = models.IntegerField(default=0)

class Ratings(models.Model):
    RID = models.IntegerField
    BID = models.ForeignKey(Book, on_delete=models.CASCADE)
    Rater = models.ForeignKey(User, on_delete=models.CASCADE)
    Rating = models.SmallIntegerField(default=0)

class Cart(models.Model):
    CartID = models.IntegerField(default=0)
     # Costumer_Email = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Cost = models.IntegerField(default=0)

class Order(models.Model):
    OID = models.IntegerField(default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    Of_Cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cost = models.CharField(max_length=50, default=0)
    status = models.CharField(max_length=50, default=0)
    address = models.CharField(max_length=200, default=0)
    postalCode = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BookCategory(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(
    Book, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Stock(models.Model):
    BID = models.ForeignKey(Book, on_delete=models.CASCADE)
    Count = models.IntegerField(default=0)


class Publisher(models.Model):
    PName = models.CharField(max_length=50)
    Num = models.IntegerField(default=0)


class CartBook(models.Model):
    BID = models.ForeignKey(Book, on_delete=models.CASCADE)
    CartID = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Count = models.IntegerField(default=0)
