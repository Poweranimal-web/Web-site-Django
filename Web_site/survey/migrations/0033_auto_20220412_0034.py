# Generated by Django 3.1.1 on 2022-04-11 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0032_auto_20220410_2227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeradminauth',
            old_name='name',
            new_name='login',
        ),
        migrations.RenameField(
            model_name='employeradminauth',
            old_name='password',
            new_name='password_e',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='password',
            new_name='password_r',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='name',
            new_name='restaurant_name',
        ),
    ]