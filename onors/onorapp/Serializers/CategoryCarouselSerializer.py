from rest_framework import serializers
from onorapp.models import CategoryCarousel

class CategoryCarouselSerializers(serializers.ModelSerializer):
    class Meta:
        model=CategoryCarousel
        fields="__all__"
