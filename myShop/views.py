from django.shortcuts import render, get_object_or_404
from .models import Category, Product



def categories_list(request):
    ctg = Category.objects.all()
    return render(request,'categories.html',{'ctg': ctg})


def products_list(request):
    prd = Product.objects.all()
    return render(request,'products.html',{'prd': prd})


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request,'category_products.html',{'ctg': category,'prd': products})

