from rest_framework import serializers
from .models import user_transactions,users

class user_transactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_transactions
        fields = '__all__'
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model =users
        fields='__all__'
