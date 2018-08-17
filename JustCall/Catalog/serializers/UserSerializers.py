from rest_framework import serializers
from Catalog.models import Users
import crypt

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
