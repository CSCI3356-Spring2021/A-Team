# Generated by Django 3.1.7 on 2021-04-23 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210423_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]
