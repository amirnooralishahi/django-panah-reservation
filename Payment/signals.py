from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Payment, RecordReserve
from Room.models import Rooms,reservation

@receiver(post_save,sender=reservation)
def create_some_atrribute(sender,instance ,created, **kwargs): 
    
    if created: 
        Payment.objects.create(
            reservation=instance, 
            passenger = instance.passenger, 
            allpaid = instance.room.price  
        )


@receiver(post_save, sender=Payment)
def create_record_reserve(sender, instance, created, **kwargs):
    check= instance.tuition != None
    if  (check):
            RecordReserve.objects.create(
                passenger=instance.passenger,
                room=instance.reservation.room,
                payment=instance
            )
            

