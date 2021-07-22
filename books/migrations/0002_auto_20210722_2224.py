# Generated by Django 3.2.5 on 2021-07-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='languages',
            field=models.ManyToManyField(related_name='books', related_query_name='book', to='books.Language'),
        ),
        migrations.AddField(
            model_name='book',
            name='themes',
            field=models.ManyToManyField(related_name='books', related_query_name='book', to='books.Theme'),
        ),
    ]
