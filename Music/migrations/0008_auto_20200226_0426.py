# Generated by Django 2.2 on 2020-02-26 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0007_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.FileField(default='Music/images/', max_length=1000, upload_to=''),
        ),
    ]
