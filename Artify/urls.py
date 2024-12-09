from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include('Artify.categories.urls')),  # Categories URLs
    path('orders/', include('Artify.categories.urls')),  # Orders URLs
    path('profiles/', include('Artify.categories.urls')),  # Profiles URLs
    path('artworks/', include('Artify.categories.urls')),  # Artworks URLs
    path('reviews/', include('Artify.categories.urls')),  # Reviews URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Login, logout, etc.
]

