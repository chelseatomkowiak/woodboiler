from django.contrib import admin
from django.urls import path, include

from interfaceapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('interfaceapp.urls')),
]