from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.models import Product, Category
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.services import get_product_from_cache, get_products_in_category


class HomeListView(ListView):
    model = Product

    def get_queryset(self):
        return get_product_from_cache()


class ProductsInCategoriesList(ListView):
    model = Product
    template_name = "catalog/product_by_category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_id"] = Category.id
        return context

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return get_products_in_category(category_id=category_id)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class BaseTemplateView(TemplateView):
    template_name = "catalog/base.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.save()
        return redirect("catalog:product_detail", product.pk)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("product.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("product.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied
