from rest_framework import serializers
from .models import sports,player


class sportsSerializer(serializers.ModelSerializer):

    class Meta:
        model = sports
        fields = '__all__'

class playerSerializer(serializers.ModelSerializer):
    class Meta:
        model = player
        fields = '__all__'
        depth = 1
