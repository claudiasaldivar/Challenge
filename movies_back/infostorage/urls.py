from django.urls import path
from . import views

urlpatterns = [
    path('contries/', views.getCountries),
    path('create/', views.addCountry),
    path('read/<str:pk>/', views.getCountry),
    
    path('cities/', views.getCities),
    path('create-city/', views.addCity),
    path('read-city/<str:pk>/', views.getCity),
    
    path('address/', views.getAllAddress),
    path('create-address/', views.addAddress),
    path('read-address/<str:pk>/', views.getAddress),
    
]