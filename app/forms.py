from django import forms
from .models import *
from django.core.exceptions import ValidationError

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

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer']
        labels = {
            'customer': 'Cliente',
        }

        def save(self, commit=True):
            order = super().save(commit=False)
            order.status = 'pending'
            if commit:
                order.save()
            return order

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'item', 'quantity', 'total_price']
        labels = {
            'order': 'Pedido',
            'item': 'Item',
            'quantity': 'Quantidade',
            'total_price': 'Preço Total',
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['customer', 'rating', 'comments']
        labels = {
            'customer': 'Cliente',
            'rating': 'Avaliação',
            'comments': 'Comentários',
        }
        widgets = {
            'rating': forms.NumberInput(attrs={'placeholder': '1-5', 'min': 1, 'max': 5}),
            'comments': forms.Textarea(attrs={'placeholder': 'Deixe seus comentários aqui...'}),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise ValidationError('A avaliação deve estar entre 1 e 5.')
        return rating