from django.urls import path, include

from store.views import ProductTypeViewSet, ProductList, ProductDetail

urlpatterns = [
    path("types/", ProductTypeViewSet.as_view({"get": "list"}), name="product-types-list"),
    path("search/", ProductList.as_view(), name="product-list"),
    path("product/<slug:slug>/", ProductDetail.as_view(), name="product-detail")
]

app_name = "store"
