from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


class HomeListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class BaseTemplateView(TemplateView):
    template_name = 'catalog/base.html'
