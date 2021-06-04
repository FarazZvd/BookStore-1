
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Category, BookCategory,User

class RegestrationSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'passwords'}, write_only=True)
    class Meta:
        model = User
        fields = [
                'username',
                'email',
                'password',
                'password2',
                'Num',
                'Province',
                'City',
                'address',
                'postal_code',
            ]
        extra_kwargs = {
                'password' : {'write_only' : True}
        }

    def save(self):
        account = User(
            email    = self.validated_data['email'],
            username = self.validated_data['username'],
            Num = self.validated_data['Num'],
            City = self.validated_data['City'],
            Province = self.validated_data['Province'],
            address = self.validated_data['address'],
            postal_code = self.validated_data['postal_code'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'پسوورد ها باید یکسان باشد'})
        account.set_password(password)
        account.save()
        return account




class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'publisher', 'author', 'summery', 'rating','Year','Price','Edition', 'image', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ['id', 'book', 'category', 'created_at', 'updated_at']

class CategoryBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory,Category
        fields = ['book', 'category']
