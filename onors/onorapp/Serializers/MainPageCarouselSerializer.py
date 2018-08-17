from rest_framework import serializers
from onorapp.models import MainPageCarousel

class MainPageCarouselSerializers(serializers.ModelSerializer):
    class Meta:
        model=MainPageCarousel
        fields="__all__"
