from django.urls import path, re_path
from api import views

urlpatterns = [
    path('status', views.status),
    path('position', views.position),
]
