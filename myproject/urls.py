from django.contrib import admin
from django.urls import path
from core.views import client_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', client_list, name='client_list'),
]