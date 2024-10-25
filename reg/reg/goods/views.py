# views.py
from django.shortcuts import render, get_object_or_404
from .models import Products, Categories

def catalog(request):
    # Получаем все продукты, которые есть в наличии
    products = Products.objects.filter(quantity__gt=0)

    # Сортировка
    sort = request.GET.get('sort', 'newest')  # По умолчанию по новизне

    if sort == 'year_desc':
        products = products.order_by('-year_of_production')
    elif sort == 'year_asc':
        products = products.order_by('year_of_production')
    elif sort == 'name_asc':
        products = products.order_by('name')
    elif sort == 'name_desc':
        products = products.order_by('-name')
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    else:
        products = products.order_by('-id')  # По новизне

    # Фильтрация по категориям
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    categories = Categories.objects.all()

    return render(request, 'goods/catalog.html', {'products': products, 'categories': categories})



# def product(request, slug):
#     product = get_object_or_404(Products, slug=slug)
    # return render(request, 'goods/product.html', {'product': product})

# def product(request, slug):

#     product = Products.objects.get(slug=slug)

#     context = {
#         'product': product
#     }

#     return render(request, 'goods/product.html', context)

def product(request, slug):
    product = Products.objects.get(slug=slug)

    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context)