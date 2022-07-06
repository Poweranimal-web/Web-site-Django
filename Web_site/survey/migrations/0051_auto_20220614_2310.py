# Generated by Django 3.1.1 on 2022-06-14 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0050_basket_price_for_one'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='address_of_restaurant',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lng',
            field=models.FloatField(default=0),
        ),
    ]
