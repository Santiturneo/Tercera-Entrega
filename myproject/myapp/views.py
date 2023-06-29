from django.shortcuts import render
from .models import Category, Product, Customer


def home(request):
    return render(request, 'home.html')


def create_data(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')

        category = Category.objects.create(name=category_name)
        product = Product.objects.create(name=product_name, price=product_price, category=category)
        customer = Customer.objects.create(name=customer_name, email=customer_email)

        return render(request, 'success.html')

    return render(request, 'create_data.html')


def search_data(request):
    if request.method == 'POST':
        query = request.POST.get('query')

        categories = Category.objects.filter(name__icontains=query)
        products = Product.objects.filter(name__icontains=query)
        customers = Customer.objects.filter(name__icontains=query)

        return render(request, 'search_results.html', {'categories': categories, 'products': products, 'customers': customers})

    return render(request, 'search_data.html')
