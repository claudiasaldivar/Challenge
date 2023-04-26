from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

#============= STAFF ==============#
#get all staff
@api_view(['GET'])
def getAllStaff(request):
    staff = Staff.objects.all()
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data) 

#get one staff
@api_view(['GET'])
def getStaff(request, pk):
    staff = Staff.objects.get(id=pk)
    serializer = StaffSerializer(staff, many=False)
    return Response(serializer.data) 

#add one staff
@api_view(['POST'])
def addStaff(request):
    serializer = StaffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)  

#============= STORE ==============#
#get all store
@api_view(['GET'])
def getAllStore(request):
    store = Store.objects.all()
    serializer = StoreSerializer(store, many=True)
    return Response(serializer.data) 

#get one store
@api_view(['GET'])
def getStore(request, pk):
    store = Store.objects.get(id=pk)
    serializer = StoreSerializer(store, many=False)
    return Response(serializer.data) 

#add one store
@api_view(['POST'])
def addStore(request):
    serializer = StoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

#============= RENTAL ==============#
#get all rental
@api_view(['GET'])
def getAllRental(request):
    rental = Rental.objects.all()
    serializer = RentalSerializer(rental, many=True)
    return Response(serializer.data) 

#get one rental
@api_view(['GET'])
def getRental(request, pk):
    rental = Rental.objects.get(id=pk)
    serializer = RentalSerializer(rental, many=False)
    return Response(serializer.data) 

#add one rental
@api_view(['POST'])
def addRental(request):
    serializer = RentalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

#============= PAYMENT ==============#
#get all payment
@api_view(['GET'])
def getAllPayment(request):
    payment = Payment.objects.all()
    serializer = PaymentSerializer(payment, many=True)
    return Response(serializer.data) 

#get one payment
@api_view(['GET'])
def getPayment(request, pk):
    payment = Payment.objects.get(id=pk)
    serializer = PaymentSerializer(payment, many=False)
    return Response(serializer.data) 

#add one payment
@api_view(['POST'])
def addPayment(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

#============= INVENTORY ==============#
#get all inventory
@api_view(['GET'])
def getAllInventory(request):
    inventory = Inventory.objects.all()
    serializer = InventorySerializer(inventory, many=True)
    return Response(serializer.data) 

#get one inventory
@api_view(['GET'])
def getInventory(request, pk):
    inventory = Inventory.objects.get(id=pk)
    serializer = InventorySerializer(inventory, many=False)
    return Response(serializer.data) 

#add one inventory
@api_view(['POST'])
def addInventory(request):
    serializer = InventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

# #update inventory
@api_view(['PUT'])
def updateInvetory(request, pk):
    inventory = Inventory.objects.get(id=pk)
    serializer = InventorySerializer(instance=inventory, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

# #delete inventory
@api_view(['DELETE'])
def deleteInventory(request, pk):
    inventory = Inventory.objects.get(id=pk)
    inventory.delete()
    return Response('inventory deleted') 

#============= CUSTOMER ==============#
#get all customer
@api_view(['GET'])
def getAllCustomer(request):
    customer = Customer.objects.annotate(total_payments=Sum('payment__amount')).order_by('-total_payments')[:5]
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data) 

#get one customer
@api_view(['GET'])
def getCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data) 

#add one customer
@api_view(['POST'])
def addCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 