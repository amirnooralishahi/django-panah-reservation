from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import User_war_struck

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
  def validate_nationalCode(self,data): 
    code = get_object_or_404(User_war_struck,NationalCode=data.get('NationalCode'))
    if code !=True: 
      return serializers.ValidationError({'nationalCode':'همچین کد ملی وجود ندارد'})
    return data
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
