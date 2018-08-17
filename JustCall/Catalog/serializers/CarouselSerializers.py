from rest_framework import serializers
from Catalog.models import Carousels

class CarouselsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousels
        fields = '__all__'
