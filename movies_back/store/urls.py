from django.urls import path
from . import views

urlpatterns = [    
    path('staff/', views.getAllStaff),
    path('create-staff/', views.addStaff),
    path('read-staff/<str:pk>/', views.getStaff),
    
    path('store/', views.getAllStore),
    path('create-store/', views.addStore),
    path('read-store/<str:pk>/', views.getStore),
    
    path('rental/', views.getAllRental),
    path('create-rental/', views.addRental),
    path('read-rental/<str:pk>/', views.getRental),
    
    path('payment/', views.getAllPayment),
    path('create-payment/', views.addPayment),
    path('read-payment/<str:pk>/', views.getPayment),
    
    path('inventory/', views.getAllInventory),
    path('create-inventory/', views.addInventory),
    path('read-inventory/<str:pk>/', views.getInventory),
    path('update-inventory/<str:pk>/', views.updateInvetory),
    path('delete-inventory/<str:pk>/', views.deleteInventory),
    
    path('customer/', views.getAllCustomer),
    path('create-customer/', views.addCustomer),
    path('read-customer/<str:pk>/', views.getCustomer),
    
]