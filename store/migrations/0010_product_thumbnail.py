# Generated by Django 4.2.5 on 2023-09-24 23:29

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0009_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                default="",
                null=True,
                upload_to=store.models.product_image_file_path,
            ),
        ),
    ]
