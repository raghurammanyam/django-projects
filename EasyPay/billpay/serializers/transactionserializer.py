from billpay.models import transactions
from rest_framework import serializers


class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transactions
        fields = '__all__'

class gettransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transactions
        fields = '__all__'
        depth=2
