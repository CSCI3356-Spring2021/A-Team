# Generated by Django 3.2 on 2021-05-08 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20210505_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookId',
            field=models.CharField(default='FJxdvMJPfAAXWuayhvjNNp', editable=False, max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sold',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]