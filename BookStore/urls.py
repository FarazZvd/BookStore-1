from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path
from django.views.static import serve
from BookStore import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path(r'api/books/', include("books.urls")),
                  path('rest-auth/', include('rest_auth.urls')),
                  path(r'registration/', include("books.urls")),
                  path('rest-auth/registration/', include('rest_auth.registration.urls')),
                  url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, })

              ] + static(settings.MEDIA_URL, document_Root=settings.MEDIA_ROOT)
