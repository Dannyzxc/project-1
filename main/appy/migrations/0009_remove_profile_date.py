# Generated by Django 4.0.4 on 2022-05-04 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0008_alter_profile_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date',
        ),
    ]