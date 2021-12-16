from django.contrib.auth.models import AbstractUser
from django.db import models


class Country(models.Model):

    name = models.CharField(max_length=160, verbose_name='название')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class Region(models.Model):

    name = models.CharField(max_length=160, verbose_name='название')
    country = models.ForeignKey(Country,
                                on_delete=models.SET_NULL,
                                null=True,
                                verbose_name='страна',
                                related_name='regions')

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return f'{self.id} - {self.name}'


class City(models.Model):

    name = models.CharField(max_length=160, verbose_name='название')
    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               null=True,
                               verbose_name='регион',
                               related_name='cities')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.id} - {self.name}'


class User(AbstractUser):

    class GenderChoice(models.TextChoices):
        MALE = 'M', 'мужской'
        FEMALE = 'F', 'женский'
        NONE = 'N', 'не указан'

    email = models.EmailField(unique=True, verbose_name='e-mail')
    birthday = models.DateField(blank=True, verbose_name='день рождения')
    gender = models.CharField(max_length=1,
                              choices=GenderChoice.choices,
                              default=GenderChoice.NONE,
                              verbose_name='пол')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='дата изменения')
    city = models.ForeignKey(City,
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name='город',
                             related_name='users')
    avatar = models.ImageField(upload_to='users_avatars', verbose_name='аватар')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Contact(models.Model):

    class ContactsChoice(models.TextChoices):
        EMAIL = 'EM', 'E-mail'
        PHONE = 'PH', 'Телефон'
        VK = 'VK', 'ВКонтакте'
        GOOGLE = 'GL', 'Google'

    name = models.CharField(max_length=2,
                            choices=ContactsChoice.choices,
                            default=ContactsChoice.EMAIL,
                            verbose_name='название')
    info = models.CharField(max_length=160, verbose_name='информация')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='contacts')
    date_created = models.DateField(auto_now_add=True, verbose_name='дата создания')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.id} - {self.name}'
