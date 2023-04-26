from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('infostorage/', include('infostorage.urls')),
    path('store/', include('store.urls')),
    path('films/', include('films.urls')),
]
