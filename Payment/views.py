from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from Room.permission import IsInspectorMember
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .models import Payment,RecordReserve
from .serializers import PaymentSer,RecordSer
from Passenger.models import  User_war_struck
# Create your views here.



#for this class url pattern is created
class ListPayment ( APIView):
  renderer_classes = [JSONRenderer]
  authentication_classes = [JWTAuthentication]
  def get_permissions(self):
    if self.request.method=='GET' : 
      return [IsInspectorMember()]
    return [AllowAny]
  def get ( self,request ):
    get_query = Payment.objects.all()
    ser = PaymentSer(get_query,many=True)
    return Response (ser.data)



#for this class url pattern is created

class DetailPayment(APIView):
  renderer_classes = [JSONRenderer]
  authentication_classes=[JWTAuthentication]

  def get_permissions(self):
    if self.request.method in ['GET','PUT']:
      return [ IsAuthenticated()]
    if self.request.method =='DELETE' : 
      return [IsAdminUser()]
    return [AllowAny]
  def get ( self , request ,passenger):
        print(Payment.objects.filter(id=17)==passenger ,'\n')
    
        instance = Payment.objects.filter(passenger=passenger)
        
        ser = PaymentSer(instance=instance,many=True)
        print(ser.data)
        return Response(ser.data)
    
  def put(self, request, passenger):
    instance = Payment.objects.get(passenger=passenger)
    ser = PaymentSer(instance, data= request.data, partial= True)
    if ser.is_valid():
      ser.save( )
      return Response(ser.data, status=status.HTTP_201_CREATED)
    return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
  def delete(self, request, passenger ):
    instance=Payment.objects.get(passenger=passenger)
    instance.delete()
    return Response({'message ':'delete successfully '})

#for this class url pattern is created

class ListRecord(APIView):
  renderer_classes = [JSONRenderer]
  authentication_classes=[JWTAuthentication]
  def get_permissions(self):
    if self.request.method in ['GET', 'POST']: 
      return [IsInspectorMember()]
    return [AllowAny]
  def get(self,request):
    instance = RecordReserve.objects.all()
    ser = RecordSer(instance,many=True)
    return Response(ser.data,status=status.HTTP_200_OK)
  def Post(self,request):
    ser = RecordSer(data=request.data)
    if ser.is_valid( ):
      ser.save()
      return Response ( ser.data, status=status.HTTP_200_OK)
    return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)


#for this class url pattern is created
class DetailRecord(APIView):
  renderer_classes = [JSONRenderer]
  authentication_classes=[JWTAuthentication]
  permission_classes=[IsAuthenticated()]
  def get ( self,request,pk):
    query=RecordReserve.objects.filter(id=pk)
    ser=RecordSer(query)
    return Response(ser.data)

  def put(self,request,pk):
    instance = RecordReserve.objects.get(id=pk )
    ser = RecordSer(instance,data=request.data,partial=True)
    if ser.is_valid( ):
      ser.save()
      return Response(ser.data,status=status.HTTP_200_OK)
    return Response (ser.errors, status= status.HTTP_400_BAD_REQUEST)

