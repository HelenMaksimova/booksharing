from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    add_info = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    add_info = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])


class Book(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='books_images', blank=True, null=True)
    isbn = models.CharField(max_length=20, null=True, blank=True)
    publish_year = models.PositiveIntegerField(default=1945)
    pages_count = models.PositiveIntegerField(default=1)
    books_count = models.PositiveIntegerField(default=1)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    authors = models.ManyToManyField(Author, related_name='books', related_query_name='book')
    languages = models.ManyToManyField(Language, related_name='books', related_query_name='book')
    themes = models.ManyToManyField(Theme, related_name='books', related_query_name='book')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name
