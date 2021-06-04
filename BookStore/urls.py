
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path
from BookStore import settings
from django.conf.urls import url

urlpatterns = [
  path('admin/', admin.site.urls),
  path(r'api/books/', include("books.urls")),
  path('rest-auth/', include('rest_auth.urls')),
  path(r'registration/', include("books.urls")),


]+static(settings.MEDIA_URL,document_Root=settings.MEDIA_ROOT)
