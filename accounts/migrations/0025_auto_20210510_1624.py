# Generated by Django 3.2 on 2021-05-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20210510_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='seller',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookId',
            field=models.CharField(default='Cb82wevMaSpicXqeRG53QY', editable=False, max_length=40, primary_key=True, serialize=False),
        ),
    ]
