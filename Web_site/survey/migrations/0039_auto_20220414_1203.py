# Generated by Django 3.1.1 on 2022-04-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0038_auto_20220414_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image_of_restaurant',
            field=models.ImageField(blank=True, upload_to='ckeditor'),
        ),
    ]