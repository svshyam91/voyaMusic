# Generated by Django 2.2 on 2020-01-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0003_auto_20200125_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracks',
            name='file_path',
            field=models.CharField(default='/home/svshyam97/Django/musicFiles/', max_length=500),
        ),
        migrations.AddField(
            model_name='tracks',
            name='image_path',
            field=models.CharField(default='/home/svshyam97/Django/musicImages/', max_length=500),
        ),
    ]
