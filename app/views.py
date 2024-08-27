from django.shortcuts import render, redirect
from .models import *
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
    return render(request, 'customer.html', {'form': form, 'customers': customers})