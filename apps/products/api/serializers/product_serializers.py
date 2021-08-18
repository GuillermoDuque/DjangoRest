from apps.products.models import Product
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        exclude = ('state',)