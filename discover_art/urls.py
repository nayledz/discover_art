from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('discover_art.art_auth.urls')),
    path('', include('discover_art.art_products.urls')),
    path('', include('discover_art.art_accounts.urls')),
    path('', include('discover_art.art_orders.urls')),
    path('', include('discover_art.art_contact.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)