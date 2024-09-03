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

def delete_category(request, category_id):
    if request.method == 'POST':
        category = Category.objects.get(pk=category_id)
        category.delete()
    return JsonResponse({'success': True})

def edit_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'menu/edit_category.html', {'form': form})

def items(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = ItemForm()
    items = MenuItem.objects.all()
    return render(request, 'menu/items.html', {'form': form, 'items': items})

def delete_item(request, item_id):
    if request.method == 'POST':
        item = MenuItem.objects.get(pk=item_id)
        item.delete()
    return JsonResponse({'success': True})

def edit_item(request, item_id):
    item = MenuItem.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = ItemForm(instance=item)
    return render(request, 'menu/edit_item.html', {'form': form})

def manage_employee(request):
    return render(request, 'employee/manage_employee.html')

def role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role')
    else:
        form = RoleForm()
    roles = Role.objects.all()
    return render(request, 'employee/role.html', {'form': form, 'roles': roles})

def delete_role(request, role_id):
    if request.method == 'POST':
        role = Role.objects.get(pk=role_id)
        role.delete()
    return JsonResponse({'success': True})

def edit_role(request, role_id):
    role = Role.objects.get(pk=role_id)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role')
    else:
        form = RoleForm(instance=role)
    return render(request, 'employee/edit_role.html', {'form': form})

def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee')
    else:
        form = EmployeeForm()
    employees = Employee.objects.all()

    return render(request, 'employee/employee.html', {'form': form, 'employees': employees})

def delete_employee(request, employee_id):
    if request.method == 'POST':
        employee = Employee.objects.get(pk=employee_id)
        employee.delete()
    return JsonResponse({'success': True})

def edit_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/edit_employee.html', {'form': form})

def manage_reserve(request):
    return render(request, 'reserve/manage_reserve.html')

def table(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table')
    else:
        form = TableForm()
    tables = Table.objects.all()
    return render(request, 'reserve/table.html', {'form': form, 'tables': tables})

def delete_table(request, table_id):
    if request.method == 'POST':
        table = Table.objects.get(pk=table_id)
        table.delete()
    return JsonResponse({'success': True})

def edit_table(request, table_id):
    table = Table.objects.get(pk=table_id)
    if request.method == 'POST':
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect('table')
    else:
        form = TableForm(instance=table)
    return render(request, 'reserve/edit_table.html', {'form': form})

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            table = form.cleaned_data['table']
            customer = form.cleaned_data['customer']
            quantity = form.cleaned_data['quantity']
            if table.capacity < quantity:
                form.add_error('quantity', 'Quantidade de pessoas excede a capacidade da mesa')
                return render(request, 'reserve/reservation.html', {'form': form})
            if table.is_available:
                table.is_available = False
                table.save()
                if not customer.has_table:
                    customer.has_table = True
                    customer.save()
                form.save()
            else:
                form.add_error('table', 'Table is not available')
            return redirect('reservation')
    else:
        form = ReservationForm()
    reservations = Reservation.objects.all()
    return render(request, 'reserve/reservation.html', {'form': form, 'reservations': reservations})


def delete_reservation(request, reservation_id):
    if request.method == 'POST':
        reservation = Reservation.objects.get(pk=reservation_id)
        table = reservation.table
        table.is_available = True
        table.save()
        customer = reservation.customer
        customer.has_table = False
        customer.save()
        reservation.delete()
    return JsonResponse({'success': True})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order/order.html', {'form': form})

def edit_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'order/order.html', {'form': form})

def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order/order_confirm_delete.html', {'order': order})

def order_item_list(request):
    order_items = OrderItem.objects.all()
    return render(request, 'order/orderitem_list.html', {'order_items': order_items})

def order_item(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orderitem_list')
    else:
        form = OrderItemForm()
    return render(request, 'order/orderitem.html', {'form': form})

def edit_order_item(request, pk):
    order_item = OrderItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=order_item)
        if form.is_valid():
            form.save()
            return redirect('orderitem_list')
    else:
        form = OrderItemForm(instance=order_item)
    return render(request, 'order/orderitem_form.html', {'form': form})

def delete_order_item(request, pk):
    order_item = OrderItem.objects.get(pk=pk)
    if request.method == 'POST':
        order_item.delete()
        return redirect('orderitem_list')
    return render(request, 'order/orderitem_confirm_delete.html', {'order_item': order_item})