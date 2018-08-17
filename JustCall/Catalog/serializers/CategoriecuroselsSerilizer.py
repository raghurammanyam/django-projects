from rest_framework import serializers
from Catalog.models import categorie_curosels

class categorie_curoselsSerializer(serializers.ModelSerializer):
    class Meta:
        model = categorie_curosels
        fields = '__all__'
