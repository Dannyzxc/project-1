# Generated by Django 4.0.4 on 2022-05-02 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0002_product_rename_name_contact_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
    ]
