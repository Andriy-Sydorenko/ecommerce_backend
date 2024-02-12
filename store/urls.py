from django.urls import include, path
from rest_framework.routers import DefaultRouter

from store.views import (ProductTypeViewSet, ProductViewSet,
                         get_sizes_for_product_type)

router = DefaultRouter()
router.register("types", ProductTypeViewSet, basename="product_type")
router.register("products", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),

    path("ajax/get_sizes_for_product_type/<int:product_type_id>/", get_sizes_for_product_type, name="ajax_get_sizes"),
]

app_name = "store"
