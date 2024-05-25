from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path

app_name = 'contacts'

urlpatterns = [
    path('get_contacts/', views.get_contacts, name='get_contacts'),
]
