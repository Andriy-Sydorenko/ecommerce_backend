from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiParameter

product_doc_parameters = [
    OpenApiParameter(
        name="product_name",
        type=OpenApiTypes.STR,
        description="Filter by product name (e.g. ?product_name=Acme%20Slip-On%20Shoes)",
    ),
    OpenApiParameter(
        name="product_price",
        type=OpenApiTypes.STR,
        description="Filter by product price (e.g. ?product_price=20 or ?product_price=20.50)"
    ),
]

product_doc_examples = [
    OpenApiExample(
        name="Filter by product name",
        description="Get products with name containing 'T-Shirt'.",
        value="?product_name=T-Shirt",
    ),
    OpenApiExample(
        name="Filter by product price",
        description="Get products with price 20.",
        value="?product_price=20",
    ),
]
