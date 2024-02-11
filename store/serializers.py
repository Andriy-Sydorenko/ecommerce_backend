from rest_framework import serializers

from store.models import Product, ProductImage, ProductType, Size

# TODO: in the final result - delete all slug in fields in serializers


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ("name", )


class ProductTypeDetailSerializer(serializers.ModelSerializer):
    sizes = SizeSerializer(many=True)

    class Meta:
        model = ProductType
        fields = "__all__"


class ProductTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ("id", "name", "slug", "is_active")


class ProductSerializer(serializers.ModelSerializer):
    product_type = ProductTypeListSerializer()

    class Meta:
        model = Product
        fields = ("id", "name", "price", "slug", "thumbnail", "product_type")


class ProductListSerializer(ProductSerializer):
    pass


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image", )


class ProductDetailSerializer(ProductSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("id", "name", "slug", "thumbnail", "images", "colors", "sizes", "description")

    def get_images(self, obj):
        images = obj.images.all()
        return ProductImageSerializer(images, many=True, context=self.context).data
