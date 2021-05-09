# Generated by Django 3.2 on 2021-05-05 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_book_bookid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookId',
            field=models.CharField(default='eADZfJFDEzR4WVLxFDW2Gz', editable=False, max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sold',
            name='count',
            field=models.IntegerField(null=True),
        ),
    ]
