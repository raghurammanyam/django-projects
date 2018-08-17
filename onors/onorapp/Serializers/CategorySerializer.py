from rest_framework import serializers
from onorapp.models import Categories

class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields="__all__"
