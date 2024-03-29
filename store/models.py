import os
import uuid

from django.db import models
from django.utils.text import slugify


class Size(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class ProductType(models.Model):

    name = models.CharField(
        max_length=255, unique=True, verbose_name="Category name", help_text="Required and unique"
    )
    sizes = models.ManyToManyField(Size, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=True)

    is_active = models.BooleanField(
        verbose_name="Product type is visible",
        help_text="Change product type visibility",
        default=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(ProductType, self).save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=["name"])
        ]

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


def product_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    base_dir = "uploads/products"
    if isinstance(instance, ProductImage):
        product_slug = slugify(instance.product.slug)
    elif isinstance(instance, Product):
        product_slug = slugify(instance.name)
    else:
        product_slug = "misc"

    filename = f"{product_slug}-{uuid.uuid4()}{extension}"
    return os.path.join(base_dir, product_slug, filename)


class Product(models.Model):
    # TODO: uncomment if needed custom UUID id field
    # id = models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True, unique=True)
    product_type = models.ForeignKey(ProductType, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=True)

    price = models.DecimalField(max_digits=5, decimal_places=2)
    thumbnail = models.ImageField(upload_to=product_image_file_path, blank=True, null=True)

    description = models.TextField(blank=True)
    stock_quantity = models.IntegerField()
    sizes = models.ManyToManyField(Size, blank=True)
    colors = models.ManyToManyField(Color, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(
        verbose_name="Product is visible",
        help_text="Change product visibility",
        default=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Product, self).save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=["name", ]),
        ]

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(null=True, upload_to=product_image_file_path, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} Image"
