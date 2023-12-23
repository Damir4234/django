from django.db import models

NULLABLE = {'blank': True, 'null': True}


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
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    purchase_price = models.FloatField(verbose_name='цена за покупку')
    date_of_creation = models.DateField(verbose_name='дата создания', auto_now_add=True)
    last_modified_date = models.DateField(verbose_name='дата последнего изменения', auto_now=True)

    def __str__(self):
        return f'{self.name} {self.description} {self.purchase_price} '

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'