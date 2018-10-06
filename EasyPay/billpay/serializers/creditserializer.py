from billpay.models import user_credits
from rest_framework import serializers


class creditSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_credits
        fields = '__all__'
