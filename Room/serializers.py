from rest_framework import serializers
from .models import Rooms,reservation,RoomImage




class ReserveSer(serializers.ModelSerializer):
  class Meta:
      model= reservation
      fields='__all__'
        
  def get_fields(self):
        fields= super().get_fields()
        for field in fields.values() : 
            field.read_only = True
        return fields
    
      
class RoomImageSer(serializers.ModelSerializer): 
    class Meta:
      model=RoomImage
      read_only_fields= ['room','upload_at']
      
class RoomSer(serializers.ModelSerializer) :
  images = RoomImageSer(many=True, read_only=True)
  class Meta:
      model=Rooms
      exclude=['id']



class RoomCreateWithImagesSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=True
    )

    class Meta:
        model = Rooms
        fields = ['id', 'name', 'images']

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

