# Generated by Django 4.2.5 on 2024-02-10 13:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0012_size_product_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="size",
            name="product_type",
        ),
        migrations.AddField(
            model_name="producttype",
            name="sizes",
            field=models.ManyToManyField(blank=True, to="store.size"),
        ),
    ]