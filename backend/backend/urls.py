from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

# Simple view function to handle the base URL
def home_view(request):
    return HttpResponse("Welcome to the Contacts App API! Visit /cotacts/ to see the contacts.")

# Alternatively, redirect to the contacts API
def home_view(request):
    return redirect('/contacts/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls')),
    path('', home_view),  # Add this line to handle the base URL
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
