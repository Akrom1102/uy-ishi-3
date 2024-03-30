from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('', include('library.urls')),
    path('', include('student.urls')),
]
