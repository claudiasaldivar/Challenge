from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

#============= LANGUAGE ==============#
#get all language
@api_view(['GET'])
def getAllLanguage(request):
    language = Language.objects.all()
    serializer = LanguageSerializer(language, many=True)
    return Response(serializer.data) 

#get one language
@api_view(['GET'])
def getLanguage(request, pk):
    language = Language.objects.get(id=pk)
    serializer = LanguageSerializer(language, many=False)
    return Response(serializer.data) 

#add one language
@api_view(['POST'])
def addLanguage(request):
    serializer = LanguageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

#============= CATEGORY ==============#
#get all category
@api_view(['GET'])
def getAllCategory(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data) 

#get one category
@api_view(['GET'])
def getCategory(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data) 

#add one category
@api_view(['POST'])
def addCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

#============= ACTOR ==============#
#get all actor
@api_view(['GET'])
def getAllActor(request):
    actor = Actor.objects.all()
    serializer = ActorSerializer(actor, many=True)
    return Response(serializer.data) 

#get one actor
@api_view(['GET'])
def getActor(request, pk):
    actor = Actor.objects.get(id=pk)
    serializer = ActorSerializer(actor, many=False)
    return Response(serializer.data) 

#add one actor
@api_view(['POST'])
def addActor(request):
    serializer = ActorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

#============= FILMS ==============#
#get all films
@api_view(['GET'])
def getAllFilms(request):
    films = Films.objects.all().order_by('-rating')[:5]
    serializer = FilmsSerializer(films, many=True)
    return Response(serializer.data) 

#get one films
@api_view(['GET'])
def getFilms(request, pk):
    films = Films.objects.get(id=pk)
    serializer = FilmsSerializer(films, many=False)
    return Response(serializer.data) 

#add one films
@api_view(['POST'])
def addFilms(request):
    serializer = FilmsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 


#============= FILMACTOR ==============#
#get all filmactor
@api_view(['GET'])
def getAllFilmActor(request):
    filmactor = FilmActor.objects.all()
    serializer = FilmActorSerializer(filmactor, many=True)
    return Response(serializer.data) 

#get one filmactor
@api_view(['GET'])
def getFilmActor(request, pk):
    filmactor = FilmActor.objects.get(id=pk)
    serializer = FilmActorSerializer(filmactor, many=False)
    return Response(serializer.data) 

#add one filmactor
@api_view(['POST'])
def addFilmActor(request):
    serializer = FilmActorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

#============= FILMCATEGORY ==============#
#get all filmcategory
@api_view(['GET'])
def getAllFilmCategory(request):
    filmcategory = FilmCategory.objects.all()
    serializer = FilmCategorySerializer(filmcategory, many=True)
    return Response(serializer.data) 

#get one filmcategory
@api_view(['GET'])
def getFilmCategory(request, pk):
    filmcategory = FilmCategory.objects.get(id=pk)
    serializer = FilmCategorySerializer(filmcategory, many=False)
    return Response(serializer.data) 

#add one filmcategory
@api_view(['POST'])
def addFilmCategory(request):
    serializer = FilmCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 