# Generated by Django 3.1.1 on 2022-04-20 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0043_dish_im'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='im',
            new_name='IM',
        ),
    ]
