# Generated by Django 3.2 on 2021-05-12 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_alter_book_bookid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookId',
            field=models.CharField(default='eWLiyu9tEUXeD7SdotmSMJ', editable=False, max_length=40, primary_key=True, serialize=False),
        ),
    ]
