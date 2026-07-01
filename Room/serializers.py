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
      read_only_fields= ['room','upload_at']
      
class RoomSer(serializers.ModelSerializer) :
  images = RoomImageSer(many=True, read_only=True)
  class Meta:
      model=Rooms
      fields='__all__'



class RoomCreateWithImagesSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User_home_owner.objects.all())
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=True
    )

    class Meta:
        model = Rooms
        fields = [
            'id',
            'owner',
            'location',
            'city',
            'Dormitory',
            'building_Information',
            'Bed_Service',
            'Toilet_Bathroom',
            'Accommodation_cap',
            'Perspective',
            'Internal_Faclities',
            'Additional_details',
            'time_reserve',
            'price',
            'images',
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

