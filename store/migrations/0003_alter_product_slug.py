# Generated by Django 4.2.5 on 2023-09-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_alter_product_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(
                default="djangodbmodelsfieldscharfield", max_length=255, unique=True
            ),
        ),
    ]
