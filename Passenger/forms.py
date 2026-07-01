from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import User_war_struck

def password_len_validator(text) : 
  if len(text)<8: 
    raise ValidationError('password must be at least 8 characters ')


class UserCreationform(forms.Form):
  email=forms.EmailField()
  username=forms.CharField(max_length=100,help_text='username must be a string')
  password1=forms.CharField(max_length=100,widget=forms.PasswordInput(),validators=[password_len_validator])
  password2=forms.CharField(max_length=100,widget=forms.PasswordInput(),validators=[password_len_validator])
 
 
class UserProfileCreationForm(forms.ModelForm): 
  class Meta:
    model = User_war_struck
    fields = '__all__'