# Generated by Django 3.2.5 on 2021-07-22 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='нет изображения', upload_to='books_images'),
        ),
    ]
