# Generated by Django 3.1.1 on 2022-04-09 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0020_auto_20220409_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='type_of_cuisine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.cuisine'),
        ),
    ]