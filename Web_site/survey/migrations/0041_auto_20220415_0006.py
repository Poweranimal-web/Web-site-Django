# Generated by Django 3.1.1 on 2022-04-14 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0040_auto_20220414_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='currency',
        ),
        migrations.AddField(
            model_name='dish',
            name='currency',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='survey.currency'),
            preserve_default=False,
        ),
    ]