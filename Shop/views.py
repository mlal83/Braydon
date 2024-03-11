from django.shortcuts import render, get_object_or_404, reverse
from .models import Product


# Create your views here.



def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    return render(request, 'shop/product_detail.html', {'product': product})