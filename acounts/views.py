from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'acounts/dashboard.html')

def customer(request):
    return render(request, 'acounts/customer.html')

def products(request):
    return render(request, 'acounts/products.html')

