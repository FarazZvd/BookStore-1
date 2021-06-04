from django.contrib.auth.models import User
from django.shortcuts import render
# Create your views here.
from .serializer import BookSerializer,CategoryBookSerializer
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import viewsets, filters, generics
from .models import Book, Order,Cart #add is
from rest_framework.permissions import (
AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
)
#add is for cart
from django.views import View
from django.http import JsonResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
#add is for cart
#add is for registry
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import RegestrationSerializers
from rest_framework.authtoken.models import Token
#add is for registry

@api_view(['POST',])
def OwnerRegister(request):
    if request.method == 'POST':
        serializer = RegestrationSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            account  = serializer.save()
            data['response'] = "register successfully done"
            data['email'] = account.email
            data['username'] = account.username
            data['Num'] = account.Num
            data['Province'] = account.Province
            data['City'] = account.City
            data['address'] = account.address
            data['postal_code'] = account.postal_code
            # token = Token.objects.get(user=account).key
            # data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


class ShoppingCart(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        p_CartID = data.get('CartID')
        p_Email = data.get('Costumer_Email')
        p_Cost = data.get('Cost')

        product_data = {
            'CartID': p_CartID,
            'Costumer_Email': p_Email,
            'p_Cost': Cost,
        }

        cart_item = Cart.objects.create(**product_data)

        data = {
            "message": f"New item added to Cart with id: {cart_item.CartID}"
        }
        return JsonResponse(data, status=201)



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

class BookUpdate(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookDelete(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

class BookSearch(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ['name','author']
    ordering_fields = ['name', 'author']

class CategoryBook(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = CategoryBookSerializer
    lookup_field = 'category'
