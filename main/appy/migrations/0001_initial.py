# Generated by Django 4.0.4 on 2022-04-22 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=550)),
                ('date', models.DateField()),
            ],
        ),
    ]
