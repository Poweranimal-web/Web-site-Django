# Generated by Django 3.1.1 on 2022-03-30 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0016_auto_20220330_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerAdminAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=50)),
            ],
        ),
    ]