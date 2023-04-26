from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

#get all countries
@api_view(['GET'])
def getCountries(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data) 

#get one country
@api_view(['GET'])
def getCountry(request, pk):
    country = Country.objects.get(id=pk)
    serializer = CountrySerializer(country, many=False)
    return Response(serializer.data) 

#add one country
@api_view(['POST'])
def addCountry(request):
    serializer = CountrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

# #update country
# @api_view(['PUT'])
# def updateCountry(request, pk):
#     country = Country.objects.get(id=pk)
#     serializer = CountrySerializer(instance=country, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data) 

# #delete country
# @api_view(['DELETE'])
# def deleteCountry(request, pk):
#     country = Country.objects.get(id=pk)
#     country.delete()
#     return Response('Country deleted') 

#=============CITIES ==============#
#get all cities
@api_view(['GET'])
def getCities(request):
    countries = City.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data) 

#get one city
@api_view(['GET'])
def getCity(request, pk):
    city = City.objects.get(id=pk)
    serializer = CitySerializer(city, many=False)
    return Response(serializer.data) 

#add one city
@api_view(['POST'])
def addCity(request):
    serializer = CitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

#============= ADDRESS ==============#
#get all address
@api_view(['GET'])
def getAllAddress(request):
    address = Address.objects.all()
    serializer = AddressSerializer(address, many=True)
    return Response(serializer.data) 

#get one address
@api_view(['GET'])
def getAddress(request, pk):
    address = Address.objects.get(id=pk)
    serializer = AddressSerializer(address, many=False)
    return Response(serializer.data) 

#add one address
@api_view(['POST'])
def addAddress(request):
    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 