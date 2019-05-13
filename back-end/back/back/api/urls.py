from django.urls import path
from api import views
from api.view import authViews

urlpatterns = [
    path('status/', views.status),  # CREATE
    path('company/<int:pk>/', views.CompanyView.as_view()),  # UPDATE, GET, DELETE
    path('company/', views.CompanyView.as_view()),  # CREATE
    path('position/', views.position),  # CREATE   TODO send only foreign key

    path('users/', views.UsersListCreate.as_view()),

    path('login/', views.login),
    path('logout/', views.logout),
]
