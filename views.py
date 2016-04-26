from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import json
from .models import Category, Product, Vendor
from django.utils import timezone
import random

def compare(request):
    template = loader.get_template('pcomparer/home.html')
    return HttpResponse(template.render({}, request))

def get_product_names(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(name__icontains=q, vendor_id=9)
        results = []
        for product in products:
            product_json = {}
            product_json = product.name
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def compare_products(request):
    template = loader.get_template('pcomparer/compare.html')
    if request.POST:
        product_name = request.POST.get('product')
    else:
        return HttpResponseRedirect('/compare')
    products = Product.objects.filter(name=product_name).order_by('price')
    return HttpResponse(template.render({'products': products}, request))

def jsontomodel(request):
    with open("/home/abhai/Django/abhaisasidharan/comparo/amazonproducts.json") as file:
        data = json.load(file)
        flipkartproducts(data)

    with open("/home/abhai/Django/abhaisasidharan/comparo/amazonproducts.json") as file:
        data = json.load(file)
        amazonproducts(data)

    return HttpResponse("Importing to database...")

def flipkartproducts(data):
    vendor = Vendor(name="Flipkart")
    vendor.save()

    for item in data:
        category_name = item["category"]
        category = Category(name=category_name, time=timezone.now())
        category.save()
        for p_item in item["products"]:
            product_name = p_item["name"]
            product_ratings = 0
            product_stars = p_item["stars"]
            product_price = p_item["price"]
            product_price = product_price.strip()
            product_price = product_price.replace("Rs. ", "")
            product_price = product_price.replace(",", "")
            product_price = float(product_price)
            product = Product(name=product_name, ratings=product_ratings, stars=product_stars, price=product_price, category=category, vendor=vendor)
            product.save()

def amazonproducts(data):
    vendor = Vendor(name="Amazon")
    vendor.save()

    for item in data:
        category_name = item["category"]
        category = Category.objects.get(name=category_name)
        for p_item in item["products"]:
            product_name = p_item["name"]
            product_ratings = 0
            product_stars = p_item["stars"]
            product_price = p_item["price"]
            product_price = product_price.strip()
            product_price = product_price.replace(",", "")
            product_price = float(product_price)
            product_price = product_price + random.uniform(-4000, 4000)
            product = Product(name=product_name, ratings=product_ratings, stars=product_stars, price=product_price, category=category, vendor=vendor)
            product.save()
