# Generated by Django 3.1.1 on 2022-03-31 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0018_registration_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeradminauth',
            name='identifier',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='identifier',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image_of_restaurant',
            field=models.ImageField(default='ckeditor/e_admin/no-image.jpg', upload_to='ckeditor'),
        ),
    ]
