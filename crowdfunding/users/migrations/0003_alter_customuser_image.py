# Generated by Django 4.2.3 on 2023-08-05 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.URLField(default=None),
        ),
    ]