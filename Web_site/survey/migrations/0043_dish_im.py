# Generated by Django 3.1.1 on 2022-04-20 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0042_auto_20220415_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='im',
            field=models.CharField(default='', max_length=200),
        ),
    ]