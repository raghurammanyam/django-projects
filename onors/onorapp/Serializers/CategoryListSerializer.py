from rest_framework import serializers
from onorapp.models import CategoryList

class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model=CategoryList
        fields="__all__"
