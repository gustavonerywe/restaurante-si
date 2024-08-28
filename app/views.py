from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from .forms import *

def index(request):
    return render(request, 'index.html')


def customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')  
    else:
        form = CustomerForm()
    
    customers = Customer.objects.all() 
    return render(request, 'customer/customer.html', {'form': form, 'customers': customers})

def delete_customer(request, customer_id):
    if request.method == 'POST':
        customer = Customer.objects.get(pk=customer_id)
        customer.delete()
    return JsonResponse({'success': True})

def edit_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/edit_customer.html', {'form': form})

def menu(request):
    return render(request, 'menu/menu.html')

def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm()
    categorys = Category.objects.all()
    return render(request, 'menu/category.html', {'form': form, 'categorys': categorys})