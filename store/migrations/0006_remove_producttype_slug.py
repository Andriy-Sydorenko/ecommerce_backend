# Generated by Django 4.2.5 on 2023-09-24 14:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0005_alter_product_slug_alter_producttype_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="producttype",
            name="slug",
        ),
    ]
