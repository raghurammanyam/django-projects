from rest_framework import serializers
from onorapp.models import CategoryListImages

class CategoryListImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=CategoryListImages
        fields="__all__"
