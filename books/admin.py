from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
from .models import Book,Category,Order,BookCategory,CartBook,Publisher,Cart,Stock,Ratings,Author
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(BookCategory)
admin.site.register(CartBook)
admin.site.register(Publisher)
# admin.site.register(Costumer)
admin.site.register(Cart)
admin.site.register(Stock)
admin.site.register(Ratings)
admin.site.register(Author)




UserAdmin.fieldsets[2][1]['fields'] = ('Num','Province','City','address','postal_code',)
admin.site.register(User, UserAdmin)
