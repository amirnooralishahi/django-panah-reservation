from rest_framework import serializers
from .models import Payment,RecordReserve




class PaymentSer(serializers.ModelSerializer):
    passenger=serializers.StringRelatedField()
    class Meta:
        model = Payment
        fields='__all__'
        read_only_fields=['passenger','reservation','allpaid','debt','paymentDate']
class RecordSer(serializers.ModelSerializer):

    class Meta:
        model=RecordReserve
        fields='__all__'
        read_only_dields=['passenger','reservation','payment','date']
        
    def get_fields(self):
        fields= super().get_fields()
        for field in fields.values() : 
            field.read_only = True
        return fields
    
    
    