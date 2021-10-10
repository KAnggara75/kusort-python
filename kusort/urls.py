from django.contrib import admin
from django.urls import path, include

from apps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apps/', views.index),
    path('', views.index),
    path('bubble/', include('bubble.urls')),
]
