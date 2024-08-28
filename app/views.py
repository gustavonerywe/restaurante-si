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

def REMOVIDO(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('REMOVIDO')
    else:
        form = CategoryForm()
    REMOVIDOs = Category.objects.all()
    return render(request, 'menu/REMOVIDO.html', {'form': form, 'REMOVIDOs': REMOVIDOs})

def delete_REMOVIDO(request, REMOVIDO_id):
    if request.method == 'POST':
        REMOVIDO = Category.objects.get(pk=REMOVIDO_id)
        REMOVIDO.delete()
    return JsonResponse({'success': True})

def edit_REMOVIDO(request, REMOVIDO_id):
    REMOVIDO = Category.objects.get(pk=REMOVIDO_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=REMOVIDO)
        if form.is_valid():
            form.save()
            return redirect('REMOVIDO')
    else:
        form = CategoryForm(instance=REMOVIDO)
    return render(request, 'menu/edit_REMOVIDO.html', {'form': form})