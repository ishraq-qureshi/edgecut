# Generated by Django 3.2.6 on 2021-08-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='featured_image',
            field=models.ImageField(default='uploads/blog/default.png', upload_to='uploads/blog'),
            preserve_default=False,
        ),
    ]