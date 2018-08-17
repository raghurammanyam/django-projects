from rest_framework import serializers
from onorapp.models import Carousel

class CarouselSerializers(serializers.ModelSerializer):
    class Meta:
        model=Carousel
        fields="__all__"
