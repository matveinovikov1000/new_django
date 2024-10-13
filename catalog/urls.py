from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, base, contacts, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('base/', base, name='base'),
    path('product/<int:pk>/', product_detail, name='product_detail')
]