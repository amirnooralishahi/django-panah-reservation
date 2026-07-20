from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Rooms,reservation,RoomImage,User_home_owner
from .serializers import RoomSer,RoomCreateWithImagesSerializer,ReserveSer,RoomImageSer,ReservationDateSerializer,MyRoomSer,MyReservationSerializer
from .permission import IsInspectorMember
 # Create your views here.


from django.db.models import Q

class RoomCreateWithImagesView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    renderer_classes = [JSONRenderer]
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]

    def get(self, request):

        rooms = Rooms.objects.all()

        # جستجوی شهر یا موقعیت
        city = request.query_params.get("city")
        if city:
            rooms = rooms.filter(
                Q(city__icontains=city) |
                Q(location__icontains=city)
            )

        # سرویس خواب
        bed_service = request.query_params.get("bed_service")
        if bed_service:
            rooms = rooms.filter(
                Bed_Service__icontains=bed_service
            )

        # ظرفیت
        capacity = request.query_params.get("capacity")
        if capacity:
            rooms = rooms.filter(
                Accommodation_cap__icontains=capacity
            )

        # قیمت
        price = request.query_params.get("price")
        if price:
            if price == "free":
                rooms = rooms.filter(
                    Q(price="0") |
                    Q(price="0.0") |
                    Q(price="0.00") |
                    Q(price__iexact="رایگان")
                )
            else:
                rooms = rooms.filter(
                    price__icontains=price
                )

        serializer = RoomSer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            owner = User_home_owner.objects.get(user=request.user)
        except User_home_owner.DoesNotExist:
            return Response(
                {"message": "فقط میزبان میتواند اقامتگاه ثبت کند"},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = RoomCreateWithImagesSerializer(data=request.data)

        if serializer.is_valid():
            room = serializer.save(owner=owner)

            return Response(
                RoomSer(room).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
#for this class url pattern is created
class RoomDetail(APIView): 
  renderer_classes = [JSONRenderer]
  authentication_classes=[JWTAuthentication]
  def get_permissions(self):
     if self.request.method in ['PUT', 'DELETE']:
       return [IsAuthenticated()]
     return [AllowAny()]
  def get(self, request, pk):
    try:
      instance = Rooms.objects.get(id=pk)
    except Rooms.DoesNotExist:
      return Response({'message': 'this room is not available'}, status=status.HTTP_404_NOT_FOUND)
    ser = RoomSer(instance=instance)
    return Response(ser.data, status=status.HTTP_200_OK)
  
  def put(self,request, pk ) :
    instance=get_object_or_404(Rooms,id=pk,owner__user=request.user)
    if instance.owner.user !=request.user : 
      return Response ( {'message' : "شما اجازه ویرایش این اقامتگاه را ندارید "}, 
                       status=status.HTTP_403_FORBIDDEN)
    ser= RoomSer(instance,data=request.data,partial=True)
    if ser.is_valid( ):
      ser.save( )
      return Response(ser.data,status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
  def delete(self, request, pk):
    try:
      instance =get_object_or_404(Rooms,id=pk,owner__user=request.user)
      if instance.owner.user !=request.user: 
        return Response( {'message': "شما اجازه حذف این اقامتگاه و نداری"})
      
    except Rooms.DoesNotExist:
      return Response({'message': 'instance not found'}, status=status.HTTP_404_NOT_FOUND)
    instance.delete()
    return Response({'message': 'room deleted successfully'}, status=status.HTTP_200_OK)
    
class reserveRoom(APIView):
  renderer_classes = [JSONRenderer]
  authentication_classes=[JWTAuthentication]
  def get_permissions(self):
     if self.request.method == 'GET': 
        return [IsInspectorMember()] 
     return [AllowAny()]
  def get(self, request):
    instance = reservation.objects.all()
    ser = ReserveSer(instance=instance, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)
  def post ( self, request) : 
    ser = ReserveSer(data=request.data )
    if ser.is_valid(): 
      ser.save()
      return Response({'message':'with successfully saved '},status=status.HTTP_201_CREATED)
    return Response({'message':'error'} , status=status.HTTP_400_BAD_REQUEST)
  
  
class detailReserveRoom(APIView): 
    renderer_classes = [JSONRenderer]
    authentication_classes=[JWTAuthentication]
    
    def get_permissions(self):
       if self.request.method in ['PUT','GET','DELETE']: 
         return [IsAuthenticated()]
       return [AllowAny()]
    def get(self, request, pk):
      try:
        instance = reservation.objects.get(id=pk)
      except reservation.DoesNotExist:
        return Response({'message': 'reservation not found'}, status=status.HTTP_404_NOT_FOUND)
      ser = ReserveSer(instance=instance)
      return Response(ser.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
      try:
        instance = reservation.objects.get(id=pk)
      except reservation.DoesNotExist:
        return Response({'message': 'reservation not found'}, status=status.HTTP_404_NOT_FOUND)
      ser = ReserveSer(instance=instance, partial=True, data=request.data)
      if ser.is_valid():
        ser.save()
        return Response({'message': 'with successfully updated'}, status=status.HTTP_202_ACCEPTED)
      return Response({'message': 'error', 'errors': ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk ): 
      instance = get_object_or_404(reservation,id=pk)
      instance.delete()
      return Response({'detail':'رزرو حذف شد'},status=status.HTTP_202_ACCEPTED)
    

    
class uploadImage(APIView): 
  renderer_classes = [JSONRenderer]
  authentication_classes=[JWTAuthentication]
  
  def get_permissions(self):
    if self.request.method == 'GET': 
      return [ IsAuthenticated()]
    return []
  def get(self,request): 
    instance =RoomImage.objects.all()
    ser= RoomImageSer(instance=instance,many=True)
    return Response(ser.data,status=status.HTTP_200_OK)
  
  def post(self, request):
    ser = RoomImageSer(data=request.data)
    if ser.is_valid():
      ser.save()
      return Response({'message': 'image uploaded successfully'}, status=status.HTTP_201_CREATED)
    return Response({'message': 'invalid data', 'errors': ser.errors}, status=status.HTTP_400_BAD_REQUEST)
  
  class detailUploadImage(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = [JWTAuthentication]

    def get(self, request, pk):
      instance = RoomImage.objects.get(pk=pk)
      ser = RoomImageSer(instance=instance)
      return Response(ser.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):   
      instance = RoomImage.objects.get(id= pk) 
      ser = RoomImageSer(instance=instance,data=request.data,partial=True)
      if ser.is_valid():
         ser.save()
         return Response(ser.data,status=status.HTTP_202_ACCEPTED)
      return Response(status=status.HTTP_401_UNAUTHORIZED)  
    def delete(self,request,pk): 
      instance = RoomImage.objects.get(id=pk)
      if instance.DoesNotExist: 
        return Response({'message':'this image is not available'},status=status.HTTP_404_NOT_FOUND)
      instance.delete()
      return Response({'message':'with successfully deleted'})
    


class RoomReservationList(APIView):

    permission_classes = [AllowAny]

    def get(self, request, room_id):

        reservations = reservation.objects.filter(room_id=room_id)

        serializer = ReservationDateSerializer(
            reservations,
            many=True
        )

        return Response(serializer.data)

class MyRoomsView(APIView):

    renderer_classes = [JSONRenderer]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        profile = User_home_owner.objects.get(user=request.user)

        rooms = Rooms.objects.filter(owner=profile)

        serializer = MyRoomSer(
            rooms,
            many=True
        )

        return Response(serializer.data)
      
class MyReservationsView(APIView):

    renderer_classes = [JSONRenderer]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        reservations = reservation.objects.filter(
            passenger__user=request.user
        ).select_related("room").prefetch_related("room__images")

        serializer = MyReservationSerializer(
            reservations,
            many=True
        )

        return Response(serializer.data)