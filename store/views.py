from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from store.models import Product, ProductType, Size
from store.serializers import (ProductDetailSerializer, ProductListSerializer,
                               ProductSerializer, ProductTypeDetailSerializer,
                               ProductTypeListSerializer)


class StandardPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 40


# TODO: make that thumbnail by default is the first image in the list of images
class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeListSerializer
    lookup_field = "slug"
    pagination_class = StandardPagination

    def get_serializer_class(self):
        if self.action == "list":
            return ProductTypeListSerializer
        if self.action == "retrieve":
            return ProductTypeDetailSerializer

        return ProductTypeListSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related("sizes", "colors").all()
    serializer_class = ProductListSerializer
    lookup_field = "slug"
    pagination_class = StandardPagination

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        if self.action == "retrieve":
            return ProductDetailSerializer

        return ProductSerializer


def get_sizes_for_product_type(request, product_type_id: int):
    sizes = Size.objects.filter(product__product_type_id=product_type_id).values("id", "name")
    return JsonResponse(list(sizes), safe=False)
