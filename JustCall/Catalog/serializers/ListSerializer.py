from rest_framework import serializers
from Catalog.models import List_Of_Items

class List_Of_ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = List_Of_Items
        fields = '__all__'
