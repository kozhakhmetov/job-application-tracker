from django.urls import path
from api.views import base, auth

urlpatterns = [
    path('status/', base.status),  # CREATE
    path('company/<int:pk>/', base.CompanyView.as_view()),  # UPDATE, GET, DELETE
    path('companies/', base.CompanyView.as_view()),  # CREATE
    path('position/', base.position),  # CREATE   TODO send only foreign key

    path('users/', auth.UsersListCreate.as_view()),

    path('login/', auth.login),
    path('logout/', auth.logout),
]
