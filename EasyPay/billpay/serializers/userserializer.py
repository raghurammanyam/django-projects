from billpay.models import users
from rest_framework import serializers


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'
