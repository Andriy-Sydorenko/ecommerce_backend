from django.shortcuts import render
from rest_framework import viewsets, mixins, generics

from store.models import Product, ProductType
from store.serializers import ProductSerializer, ProductTypeSerializer, ProductDetailSerializer, ProductListSerializer


# TODO: make that thumbnail by default is the first image in the list of images
class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Product.objects.prefetch_related("sizes", "colors").all()
    serializer_class = ProductListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductDetail(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
