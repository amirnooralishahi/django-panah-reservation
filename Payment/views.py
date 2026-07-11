from decimal import Decimal
from datetime import timedelta,datetime
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from Room.permission import IsInspectorMember
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .models import Payment,RecordReserve
from .serializers import PaymentSer,RecordSer
from Passenger.models import  User_war_struck
from Room.models import reservation, Rooms




class ListPayment ( APIView):
  renderer_classes = [JSONRenderer]
  authentication_classes = [JWTAuthentication]
  def get_permissions(self):
    if self.request.method=='GET' : 
      return [IsInspectorMember()]
    return [AllowAny()]
  def get ( self,request ):
    get_query = Payment.objects.all()
    ser = PaymentSer(get_query,many=True)
    return Response (ser.data)

  def post(self, request):
    print(request.data)
    room_id = request.data.get('room_id')
    amount = request.data.get('amount')
    passenger_slug = request.data.get('passenger_slug')
    reserve_date = request.data.get('reserve_date')
    delivery_date = request.data.get('delivery_date')

    if not room_id or not amount:
      return Response({'error': 'room_id and amount are required'}, status=status.HTTP_400_BAD_REQUEST)

    room = get_object_or_404(Rooms, id=room_id)
    print(room)
    if passenger_slug:
      passenger = get_object_or_404(User_war_struck, slug=passenger_slug)
      print(passenger)
    elif request.user.is_authenticated:
      passenger = get_object_or_404(User_war_struck, user=request.user)
      print(passenger)
    else:
      return Response({'error': 'passenger information is required'}, status=status.HTTP_400_BAD_REQUEST)

    reservation_date =  datetime.strptime(
    reserve_date,
    "%Y-%m-%d"
    )
    delivery_datetime =  datetime.strptime(
    delivery_date,
    "%Y-%m-%d"
)
    reservation_obj, _ = reservation.objects.get_or_create(
        passenger=passenger,
        room=room,
        ReservDate=reservation_date,
        DeliveryDate= delivery_date
        
    )
    print(reservation_obj)
    print(reservation_obj.id)
    print("reservation id =", reservation_obj.id)
    print("reservation slug =", reservation_obj.slug)
    
    days = (delivery_datetime - reservation_date).days
    if days <= 0:
        return Response(
            {"error": "تاریخ خروج باید بعد از تاریخ ورود باشد."},
            status=status.HTTP_400_BAD_REQUEST
        )

    total_price = room.price * days

    amount = Decimal(str(amount))

    if amount > total_price:
      return Response(
        {"error": "مبلغ پرداختی بیشتر از مبلغ کل رزرو است."},
        status=status.HTTP_400_BAD_REQUEST
    )

    payment, created = Payment.objects.get_or_create(
        reservation=reservation_obj,
        
    )
    payment.allpaid = total_price
    payment.tuition = amount
    payment.save()
    
    print('payment id',payment.id)
    print('created=', created)
    print("room.price =", room.price)
    print("payment.allpaid =", payment.allpaid)
    print("amount =", amount)
    if amount > payment.allpaid:
      return Response(
          {
              "error": "مبلغ پرداختی بیشتر از مبلغ اقامتگاه است."
          },
          status=status.HTTP_400_BAD_REQUEST
      )
    if not created:
      payment.tuition = amount
      payment.save()
    return Response({
        'message': 'payment created successfully' if created else 'payment already existed and was updated',
        'payment': {
            'id': payment.id,
            'amount': str(payment.allpaid),
            'reservation_slug': reservation_obj.slug,
            'room_id': room.id,
        }
    }, status=status.HTTP_201_CREATED)




class DetailPayment(APIView):
  renderer_classes = [JSONRenderer]
  authentication_classes=[JWTAuthentication]

  def get_permissions(self):
    if self.request.method in ['GET','PUT']:
      return [IsAuthenticated()]
    if self.request.method =='DELETE' : 
      return [IsAdminUser()]
    return [AllowAny()]
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


class ListRecord(APIView):
  renderer_classes = [JSONRenderer]
  authentication_classes=[JWTAuthentication]
  def get_permissions(self):
    if self.request.method in ['GET', 'POST']:
      return [IsInspectorMember()]
    return [AllowAny()]
  def get(self, request):
    instance = RecordReserve.objects.all()
    ser = RecordSer(instance, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)
  def post(self, request):
    ser = RecordSer(data=request.data)
    if ser.is_valid():
      ser.save()
      return Response(ser.data, status=status.HTTP_200_OK)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


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

