from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Удаляем все категории
        Category.objects.all().delete()

        # Список категорий
        categories_list = [
            {"name": "Смартфоны", "description": "Категория смартфонов"},
            {"name": "Ноутбуки и ПК", "description": "Категория ноутбуков и компьютеров"},
            {"name": "Телевизоры и Аудио",
                "description": "Категория телевизоров и аудиоустройств"},
            {"name": "Фото- и Видеокамеры",
                "description": "Категория фото- и видеокамер"},
            {"name": "Гаджеты и Умные устройства",
                "description": "Категория гаджетов и умных устройств"},
            {"name": "Игровые консоли и Аксессуары",
                "description": "Категория игровых консолей и аксессуаров"},
            {"name": "Аксессуары и Зарядные устройства",
                "description": "Категория аксессуаров и зарядных устройств"}
        ]

        categories_for_create = []
        for category_item in categories_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_for_create)
