from django.contrib import admin
from django.urls import path, include
from .views import home_redirect

urlpatterns = [
    path('', home_redirect, name='home_redirect'),
    path('admin/', admin.site.urls),
    path('api/', include('projects.urls')),
]
