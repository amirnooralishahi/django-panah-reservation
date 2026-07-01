from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import User_war_struck
from .serializers import SerializersUser
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from .models import User_war_struck


class LogoutView(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request):
        response = Response({"message": "Logged out"})
        response.delete_cookie("access_token")
        return response

class CustomLoginView(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            res = Response({"message": "login successful"})

            # ست کردن کوکی HttpOnly
            res.set_cookie(
                key='access_token',
                value=str(refresh.access_token),
                httponly=True,
                secure=False,  # در production بذار True
                samesite='Lax',
                max_age=3600
            )
            return res
        else:
            return Response({"error": "Invalid credentials"}, status=401)

#برای دیدن تمامی کاربران فقط به مالک و بازرس باید سطح دسترسی بدهم 
class PassengerList (APIView):
  renderer_classes = [JSONRenderer]
  authentication_classes=[JWTAuthentication]
  def get_permissions(self):
    if self.request.method=='GET': 
      return [IsAdminUser()]
    if self.request.method =='POST': 
      return [AllowAny()]
    return [AllowAny()]
  def get (self,request,format=None):

    passenger=User_passenger.objects.all()
    ser = SerializersUser(passenger,many=True)
    return Response (ser.data)

  def post(self,request):

    ser=SerializersUser(data=request.data)
    if ser.is_valid():
      ser.save()
      return Response (ser.data,status=status.HTTP_201_CREATED)
    return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

#در این قسمت باید اول لاگین کرده باشند و بعد اجازه دیدن داشته باشند 
class PassengerDetail(APIView):
  renderer_classes = [JSONRenderer]
  authentication_classes=[JWTAuthentication]
  def get_permissions(self):
      if self.request.method in ['PUT',"DELETE"]: 
        return [ IsAuthenticated()]    
      return [AllowAny]
  def put ( self,request , pk):
      instance = User_passenger.objects.get(id=pk)
      ser = SerializersUser(instance=instance,data=request.data,partial=True)
      if ser.is_valid():
        ser.save()
        return Response(ser.data)
      return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
  def delete ( self ,pk ):
    instance=User_passenger.objects.get(id=pk)
    instance.delete()
    return Response('this user with succesfully deleted')