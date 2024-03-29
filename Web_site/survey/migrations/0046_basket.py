# Generated by Django 3.1.1 on 2022-04-22 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0045_auto_20220420_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_order', models.CharField(default='', max_length=200)),
                ('id_product', models.CharField(default='', max_length=200)),
                ('id_customer', models.CharField(default='', max_length=200)),
                ('name_of_dish', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('col', models.PositiveBigIntegerField(default=0)),
                ('add_product_at_basket', models.DateTimeField(auto_now_add=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.currency')),
            ],
        ),
    ]
