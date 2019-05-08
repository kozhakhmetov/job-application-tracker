from django.urls import path, re_path
from api import views

urlpatterns = [
    path('status/', views.status),
    path('position/', views.position),
    re_path(r'user/(\d)/', views.UserView.as_view()),
    re_path(r'company/(\d)/', views.CompanyView.as_view()),
    path('company/', views.CompanyView.as_view()),

]
