from rest_framework import serializers
from Catalog.models import Item_Pics

class Item_PicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Pics
        fields = '__all__'
