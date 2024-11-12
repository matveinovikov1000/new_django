from django.core.cache import cache

from config.settings import CACHE_ENABLED
from catalog.models import Product


def get_product_from_cache():
    """
    Получение товаров из кэша, если кэш пуст, то загрузка товеров из БД и добавлние их в кэш
    """
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)

    if products is not None:
        return products

    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_in_category(category_id):
    """Функция для выбора товара по категории"""
    products_in_category = Product.objects.filter(category_id=category_id)
    return products_in_category
