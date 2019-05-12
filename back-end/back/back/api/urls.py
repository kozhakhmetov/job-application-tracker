from django.urls import path
from api import views
from api.view import authViews

urlpatterns = [
    path('status/', views.status),
    path('position/', views.position),
    path('company/<int:pk>/', views.CompanyView.as_view()),
    path('company/', views.CompanyView.as_view()),
    # my paths
    path('users/', authViews.UsersListCreate.as_view())
]
