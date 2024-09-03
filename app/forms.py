from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']
        labels = {
            'name': 'Nome',
            'email': 'E-mail',
            'phone': 'Telefone',
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'category', 'is_available']
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'price': 'Preço',
            'category': 'Categoria',
            'is_available': 'Disponível',
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'salary', 'role']
        labels = {
            'name': 'Nome',
            'salary': 'Salário',
            'role': 'Cargo',
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'description']
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['number', 'capacity', 'is_available']
        labels = {
            'number': 'Número',
            'capacity': 'Capacidade',
            'is_available': 'Disponível',
        }

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer', 'table', 'quantity']
        labels = {
            'customer': 'Cliente',
            'table': 'Mesa',
            'quantity': 'Quantidade de Pessoas',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table'].queryset = Table.objects.filter(is_available=True)
        self.fields['customer'].queryset = Customer.objects.filter(has_table=False)
