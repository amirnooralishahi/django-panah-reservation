from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import User_war_struck, User_home_owner

class SerializersUser(serializers.ModelSerializer):
  class Meta:
    model=User_war_struck
    read_only_fields= [ 'user' , 'Is_owner','Is_inspector']
    extra_kwargs={
      'email':{'required':False}, 
      'Is_owner':{'default':False},
      'Is_inspector':{'default':False},
      'NationaCode':{'required':True}, 
      
    }
  def validate_length_nationalCode(self,data): 
    NationalCode = data.get('NationalCode')
    if NationalCode and len(NationalCode )>10 : 
      return serializers.ValidationError({'NationalCode':'کد نباید بیشتر از 10 رقم باشد'})
    return data
  def validate_nationalCode(self, data):
    national_code = data.get('NationalCode')
    if national_code and not User_war_struck.objects.filter(NationalCode=national_code).exists():
      raise serializers.ValidationError({'NationalCode': 'چنین کد ملی وجود ندارد'})
    return data

class UserProfileSerializer(serializers.ModelSerializer):
  # accept flexible phone input to avoid strict validation errors from form inputs
  phone = serializers.CharField(required=False, allow_blank=True)
  class Meta:
    model = User_war_struck
    fields = ['id', 'slug', 'email', 'phone', 'NationalCode', 'Job_title', 'picture']
    read_only_fields = ['slug', 'NationalCode']
    extra_kwargs = {
      'email': {'required': False},
      'phone': {'required': False},
      'Job_title': {'required': False},
      'picture': {'required': False},
    }

class HomeOwnerProfileSerializer(serializers.ModelSerializer):
  phone = serializers.CharField(required=False, allow_blank=True)
  class Meta:
    model = User_home_owner
    fields = ['id', 'slug', 'email', 'phone', 'NationalCode', 'Job_title', 'picture']
    read_only_fields = ['slug', 'NationalCode']
    extra_kwargs = {
      'email': {'required': False},
      'phone': {'required': False},
      'Job_title': {'required': False},
      'picture': {'required': False},
    }

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
