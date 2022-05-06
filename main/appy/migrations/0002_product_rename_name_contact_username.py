# Generated by Django 4.0.4 on 2022-05-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('price', models.IntegerField(default='100')),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='username',
        ),
    ]
