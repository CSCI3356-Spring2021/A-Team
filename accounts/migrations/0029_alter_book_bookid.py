# Generated by Django 3.2 on 2021-05-11 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20210511_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookId',
            field=models.CharField(default='5o4hACEcbXPFUnQn5pBH5s', editable=False, max_length=40, primary_key=True, serialize=False),
        ),
    ]