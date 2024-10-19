from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def contacts(request):
    return render(request, 'contacts.html')


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'home.html', context=context)


def base(request):
    return render(request, 'base.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context=context)
