from django.urls import path
from . import views

urlpatterns = [
    path('language/', views.getAllLanguage),
    path('create-language/', views.addLanguage),
    path('read-language/<str:pk>/', views.getLanguage),
    
    path('category/', views.getAllCategory),
    path('create-category/', views.addCategory),
    path('read-category/<str:pk>/', views.getCategory),
    
    path('actor/', views.getAllActor),
    path('create-actor/', views.addActor),
    path('read-actor/<str:pk>/', views.getActor),
    
    path('films/', views.getAllFilms),
    path('create-films/', views.addFilms),
    path('read-films/<str:pk>/', views.getFilms),
    
    path('filmactor/', views.getAllFilmActor),
    path('create-filmactor/', views.addFilmActor),
    path('read-filmactor/<str:pk>/', views.getFilmActor),
    
    path('filmcategory/', views.getAllFilmCategory),
    path('create-filmcategory/', views.addFilmCategory),
    path('read-filmcategory/<str:pk>/', views.getFilmCategory),
]