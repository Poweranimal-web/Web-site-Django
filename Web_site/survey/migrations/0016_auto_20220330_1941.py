# Generated by Django 3.1.1 on 2022-03-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0015_registration_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='courier',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='customer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='employer',
            field=models.BooleanField(default=False),
        ),
    ]