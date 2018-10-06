from rest_framework_mongoengine import serializers

from .models import CustomersModel,CategoriesModel,ItemsModel,OrdersModel

class CustomersModelSerializer(serializers.DocumentSerializer):
    class Meta:
        model = CustomersModel
        fields = '__all__'

class CategoriesModelSerializer(serializers.DocumentSerializer):
    class Meta:
        model = CategoriesModel
        fields = '__all__'

class ItemsModelSerializer(serializers.DocumentSerializer):
    class Meta:
        model = ItemsModel
        fields = '__all__'

class OrdersModelSerializer(serializers.DocumentSerializer):
    class Meta:
        model = OrdersModel
        fields = '__all__'
