from django.urls import path, include

from store.views import ProductTypeViewSet, ProductList, ProductDetail, get_sizes_for_product_type

urlpatterns = [
    path("types/", ProductTypeViewSet.as_view({"get": "list"}), name="product-types-list"),
    path("search/", ProductList.as_view(), name="product-list"),
    path("product/<slug:slug>/", ProductDetail.as_view(), name="product-detail"),

    path('ajax/get_sizes_for_product_type/<int:product_type_id>/', get_sizes_for_product_type, name='ajax_get_sizes'),
]

app_name = "store"
