# Generated by Django 3.2.6 on 2021-08-07 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_category_id',
            new_name='product_category',
        ),
    ]
