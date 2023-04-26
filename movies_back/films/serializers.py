from rest_framework import serializers
from .models import * 

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
        
class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'
        
class FilmActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmActor
        fields = '__all__'
        
class FilmCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmCategory
        fields = '__all__'