from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User_war_struck, User_home_owner, User
from .serializers import SerializersUser, UserProfileSerializer, HomeOwnerProfileSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


class LogoutView(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request):
        response = Response({"message": "Logged out"})
        response.delete_cookie("access_token")
        return response


class RegisterView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        national_code = request.data.get("national_code")

        if not username or not email or not password or not national_code:
            return Response({"error": "username, email, password and national_code are required"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "username already exists"}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password, user_type='war_struck')
        profile, _ = User_war_struck.objects.get_or_create(
            user=user,
            defaults={'email': email, 'NationalCode': national_code}
        )
        profile.email = email
        profile.NationalCode = national_code
        profile.save(update_fields=['email', 'NationalCode'])

        refresh = RefreshToken.for_user(user)
        response = Response({
            "message": "registered successfully",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "user_type": user.user_type,
            },
            "profile": {
                "id": profile.id,
                "slug": profile.slug,
                "NationalCode": profile.NationalCode,
                "email": profile.email,
            },
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=201)

        response.set_cookie(
            key='access_token',
            value=str(refresh.access_token),
            httponly=True,
            secure=False,
            samesite='Lax',
            max_age=3600
        )
        return response


class CustomLoginView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [AllowAny]

    def post(self, request):
      identifier = request.data.get("username") or request.data.get("identifier") or request.data.get("email") or request.data.get("phone")
      password = request.data.get("password")

      user_obj = None
      # try email
      if identifier and "@" in identifier:
        user_obj = User.objects.filter(email__iexact=identifier).first()

      # try phone in profiles
      if not user_obj and identifier:
        profile = User_war_struck.objects.filter(phone=identifier).first()
        if not profile:
          profile = User_home_owner.objects.filter(phone=identifier).first()
        if profile:
          user_obj = profile.user

      # try username
      if not user_obj and identifier:
        user_obj = User.objects.filter(username=identifier).first()

      user = None
      if user_obj:
        user = authenticate(username=user_obj.username, password=password)

      if user:
        refresh = RefreshToken.for_user(user)
        profile = User_war_struck.objects.filter(user=user).first()
        res = Response({
          "message": "login successful",
          "access": str(refresh.access_token),
          "refresh": str(refresh),
          "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "user_type": user.user_type,
          },
          "profile": {
            "id": profile.id if profile else None,
            "slug": profile.slug if profile else None,
            "NationalCode": profile.NationalCode if profile else None,
            "email": profile.email if profile else None,
          },
        })

        res.set_cookie(
          key='access_token',
          value=str(refresh.access_token),
          httponly=True,
          secure=False,
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
    if self.request.method == 'GET':
      return [IsAdminUser()]
    if self.request.method == 'POST':
      return [AllowAny()]
    return [AllowAny()]
  def get(self, request, format=None):

    passenger = User_war_struck.objects.all()
    ser = SerializersUser(passenger, many=True)
    return Response(ser.data)

  def post(self, request):

    ser = SerializersUser(data=request.data)
    if ser.is_valid():
      ser.save()
      return Response(ser.data, status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

#در این قسمت باید اول لاگین کرده باشند و بعد اجازه دیدن داشته باشند 
class PassengerDetail(APIView):
  renderer_classes = [JSONRenderer]
  authentication_classes=[JWTAuthentication]
  def get_permissions(self):
      if self.request.method in ['PUT', 'DELETE']:
        return [IsAuthenticated()]
      return [AllowAny()]
  def put(self, request, pk):
      instance = User_war_struck.objects.get(id=pk)
      ser = SerializersUser(instance=instance, data=request.data, partial=True)
      if ser.is_valid():
        ser.save()
        return Response(ser.data)
      return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
  def delete(self, request, pk):
    instance = User_war_struck.objects.get(id=pk)
    instance.delete()
    return Response('this user with succesfully deleted')

class UserProfileView(APIView):
  renderer_classes = [JSONRenderer]
  authentication_classes=[JWTAuthentication]
  permission_classes=[IsAuthenticated]

  def get_profile(self, user):
    if getattr(user, 'user_type', None) == 'home_owner':
      return User_home_owner.objects.filter(user=user).first()
    return User_war_struck.objects.filter(user=user).first()

  def get(self, request):
    profile = self.get_profile(request.user)
    if not profile:
      return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = HomeOwnerProfileSerializer(profile) if request.user.user_type == 'home_owner' else UserProfileSerializer(profile)
    return Response(serializer.data)

  def put(self, request):
    profile = self.get_profile(request.user)
    if not profile:
      return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer_class = HomeOwnerProfileSerializer if request.user.user_type == 'home_owner' else UserProfileSerializer
    serializer = serializer_class(profile, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HostRequestView(APIView):
  renderer_classes = [JSONRenderer]
  permission_classes = [AllowAny]

  def post(self, request):
    name = request.data.get('name')
    contact = request.data.get('contact')
    property_title = request.data.get('propertyTitle')
    description = request.data.get('description')

    if not name or not contact:
      return Response({'error': 'name and contact are required'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({
      'message': 'Host request received successfully',
      'data': {
        'name': name,
        'contact': contact,
        'propertyTitle': property_title,
        'description': description,
      }
    }, status=status.HTTP_201_CREATED)
