from rest_framework import serializers

from store.models import Product, ProductType, ProductImage


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id", "name", "price", "thumbnail")


class ProductListSerializer(ProductSerializer):
    pass


class ProductDetailSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "thumbnail", "image", "colors", "sizes", "description")
