from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from users.models import User

NULLABLE = {'blank': True, 'null': True}
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='products/',
                              verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    purchase_price = models.FloatField(verbose_name='цена за покупку')
    date_of_creation = models.DateField(
        verbose_name='дата создания', auto_now_add=True)
    last_modified_date = models.DateField(
        verbose_name='дата последнего изменения', auto_now=True)
    versions = models.ManyToManyField(
        'Version', related_name='products', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='products', verbose_name='пользователь')
    is_published = models.BooleanField(
        default=False, verbose_name='опубликовано')

    def __str__(self):
        return f'{self.name} {self.description} {self.purchase_price} '

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, verbose_name='id_product')
    number_version = models.IntegerField(verbose_name='номер_версии')
    name = models.CharField(max_length=100, verbose_name='наименование')
    current_version = models.BooleanField(
        verbose_name='признак_текущей_версии')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
