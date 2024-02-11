from django import forms
from django.contrib import admin
from django.forms import BaseInlineFormSet

from store.models import Color, Product, ProductImage, ProductType, Size


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.product_type_id:
            self.fields["sizes"].queryset = Size.objects.filter(producttype__id=self.instance.product_type_id)
        else:
            self.fields["sizes"].queryset = Size.objects.none()


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

    def get_queryset(self, request):
        qs = super().get_queryset(request).select_related("product")
        return qs


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [ProductImageInline, ]
    list_display = ("name", "product_type", "price", "stock_quantity", "is_active")
    search_fields = ["name", "description"]
    list_filter = ["product_type", ]
    change_form_template = "admin/product/change_form.html"

    def get_queryset(self, request):
        qs = super().get_queryset(request).select_related("product_type").prefetch_related("sizes", "colors")
        return qs


admin.site.register(ProductType)
admin.site.register(Color)
admin.site.register(Size)
