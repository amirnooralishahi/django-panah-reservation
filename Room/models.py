from django.db import models
from Passenger.models import User_war_struck,User_home_owner
from slugify import slugify
 
from uuid import uuid4

# Create your models here.
class Rooms(models.Model):
  owner = models.ForeignKey(User_home_owner, on_delete=models.CASCADE, related_name="rooms")
  location = models.CharField(max_length=200)
  city= models.CharField(max_length=100)
  Dormitory = models.CharField(max_length=200,unique=True,default=None)
  building_Information= models.CharField(max_length=400)
  Bed_Service = models.CharField(max_length=100,null=False)
  Toilet_Bathroom= models.CharField(max_length=100,null=False)
  Accommodation_cap=models.CharField(max_length=100,null=True)
  Perspective = models.TextField(null=True)
  Internal_Faclities= models.TextField(null=False)
  Additional_details = models.TextField(null=True)
  time_reserve= models.DateField(null=True)
  price = models.DecimalField(decimal_places=2,max_digits=12)
  def __str__(self):
     return f'{self.Dormitory}'
  class Meta:
     pass
class reservation(models.Model):
    passenger = models.ForeignKey(User_war_struck, on_delete=models.CASCADE, related_name="reservations")
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name="reservations")
    DeliveryDate = models.DateTimeField()
    ReservDate = models.DateTimeField()
    slug=models.SlugField(unique=True,blank=True,null=False)
    def __str__(self):
      return f'{self.passenger.user}-{self.room.location[:20]}'
    def save(self, *args, **kwargs):
      if not self.slug and self.room and self.room.Dormitory:
        dorm_name = str(self.room.Dormitory).strip()
        self.slug = dorm_name.replace(" ", "-")  # نگهداری زبان فارسی ولی تبدیل فاصله‌ها
      super().save(*args, **kwargs)

class RoomImage( models.Model): 
   room= models.ForeignKey( Rooms , related_name='images',on_delete=models.CASCADE)
   image=models.ImageField( upload_to='Room_picture')
   uploaded_at = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return f'{self.room}-{self.uploaded_at}'

