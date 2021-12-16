from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Theme(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


class Publisher(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')
    add_info = models.JSONField(blank=True, verbose_name='дополнительная информация')

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

    def __str__(self):
        return self.name


class Language(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class Author(models.Model):

    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    add_info = models.JSONField(blank=True, verbose_name='дополнительная информация')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return ' '.join([self.first_name, self.last_name])


class Book(models.Model):

    name = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')
    image = models.ImageField(upload_to='books_images', blank=True, null=True, verbose_name='обложка')
    isbn = models.CharField(max_length=20, blank=True, default='не имеет ISBN', verbose_name='ISBN')
    publish_year = models.PositiveIntegerField(default=1945, verbose_name='год публикации')
    pages_count = models.PositiveIntegerField(default=1, verbose_name='количество страниц')
    books_count = models.PositiveIntegerField(default=1, verbose_name='количество в наличии')
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  related_name='books',
                                  verbose_name='издательство')
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='books',
                                 verbose_name='категория')
    authors = models.ManyToManyField(Author, related_name='books', verbose_name='авторы')
    languages = models.ManyToManyField(Language, related_name='books', verbose_name='языки')
    themes = models.ManyToManyField(Theme, related_name='books', verbose_name='темы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.name} - {self.isbn}'
