from rest_framework import serializers
from .models import Rooms,reservation,RoomImage
from Passenger.models import User_home_owner




class ReserveSer(serializers.ModelSerializer):
  class Meta:
      model = reservation
      fields = '__all__'
    
      
class RoomImageSer(serializers.ModelSerializer): 
    class Meta:
      model=RoomImage
      fields="__all__"
      read_only_fields= ['room','uploaded_at']
      
class RoomSer(serializers.ModelSerializer) :
  images = RoomImageSer(many=True, read_only=True)
  class Meta:
      model=Rooms
      fields='__all__'



class RoomCreateWithImagesSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=True
    )

    class Meta:
        model = Rooms
        fields = [
    "id",
    'owner',
    "location",
    "city",
    "Dormitory",
    "building_Information",
    "Bed_Service",
    "Toilet_Bathroom",
    "Accommodation_cap",
    "Perspective",
    "Internal_Faclities",
    "Additional_details",
    "time_reserve",
    "price",
    "images",
]

    def validate_images(self, value):
        if not value or len(value) == 0:
            raise serializers.ValidationError("حداقل یک عکس باید ارسال شود.")
        return value

    def create(self, validated_data):
        images = validated_data.pop('images')
        room = Rooms.objects.create(**validated_data)
        for image in images:
            RoomImage.objects.create(room=room, image=image)
        return room

class ReservationDateSerializer(serializers.ModelSerializer):

    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()

    class Meta:
        model = reservation
        fields = ["start", "end"]

    def get_start(self, obj):
        return obj.ReservDate.date()

    def get_end(self, obj):
        return obj.DeliveryDate.date()
    
class MyRoomSer(serializers.ModelSerializer): 
    images = RoomImageSer(many=True,read_only=True)
    class Meta : 
        model = Rooms 
        fields='__all__'
        

class MyReservationSerializer(serializers.ModelSerializer):

    room_name = serializers.CharField(
        source="room.Dormitory",
        read_only=True
    )

    city = serializers.CharField(
        source="room.city",
        read_only=True
    )

    image = serializers.SerializerMethodField()

    class Meta:
        model = reservation
        fields = [
            "id",
            "room_name",
            "city",
            "ReservDate",
            "DeliveryDate",
            "image",
        ]

    def get_image(self, obj):

        first = obj.room.images.first()

        if first:
            return first.image.url

        return None