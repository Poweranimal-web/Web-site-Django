# Generated by Django 3.1.1 on 2022-04-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0030_auto_20220410_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
