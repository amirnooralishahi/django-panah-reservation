from django.db import models
from Passenger.models import User_war_struck,User_home_owner
from Room.models import reservation,Rooms
from decimal import Decimal
# Create your models here.
class Payment( models.Model):
  passenger = models.ForeignKey(User_war_struck,on_delete=models.CASCADE,unique=False,to_field='slug')
  reservation = models.ForeignKey(reservation, on_delete=models.CASCADE,unique=False,to_field='slug')
  allpaid= models.DecimalField(max_digits=12,decimal_places=2,default=None)
  tuition =models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
  debt = models.DecimalField(max_digits=12,decimal_places=2,blank=True,null=True)
  paymentDate=models.DateField(auto_now_add=True)

  class Meta:

        constraints = [
            models.UniqueConstraint(fields=[ 'reservation'], name='unique_payment_per_reservation')
        ]
  def save(self, *args, **kwargs):
    if self.allpaid is not None and self.tuition is not None:
        self.debt = max(
            Decimal(self.allpaid) - Decimal(self.tuition),
            Decimal("0")
        )

    super().save(*args, **kwargs)
  def __str__(self):
       return f'{self.tuition}-{self.debt}-{self.pk}'

class RecordReserve(models.Model):
    passenger = models.ForeignKey(User_war_struck,on_delete=models.CASCADE)
    room=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    payment= models.OneToOneField(Payment,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.passenger}-{self.date}'


