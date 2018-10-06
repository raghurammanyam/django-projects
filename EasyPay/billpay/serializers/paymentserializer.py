from billpay.models import payments
from rest_framework import serializers


class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payments
        fields = '__all__'

    
