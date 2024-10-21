from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    HomeListView,
    BaseTemplateView,
    ContactsTemplateView,
    ProductDetailView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeListView.as_view(), name="home"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("base/", BaseTemplateView.as_view(), name="base"),
    path("product/<int:pk>/", ProductDetailView.as_view(),
         name="product_detail"),
]
