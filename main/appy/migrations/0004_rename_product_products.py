# Generated by Django 4.0.4 on 2022-05-02 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0003_remove_product_subcategory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='product',
            new_name='products',
        ),
    ]
