from django import forms
from .models import Expense, Income, Budget


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense

        fields = [
            'title',
            'amount',
            'category',
            'payment_method',
            'date',
            'description',
        ]

        widgets = {

            'title': forms.TextInput(attrs={
                'placeholder': 'e.g. Lunch',
                'class': 'form-input',
            }),

            'amount': forms.NumberInput(attrs={
                'placeholder': 'e.g. 250',
                'step': '0.01',
                'min': '0.01',
                'class': 'form-input',
            }),

            'category': forms.Select(attrs={
                'class': 'form-input',
            }),

            'payment_method': forms.Select(attrs={
                'class': 'form-input',
            }),

            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-input',
                }
            ),

            'description': forms.Textarea(attrs={
                'placeholder': 'Optional description',
                'rows': 4,
                'class': 'form-input',
            }),
        }


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income

        fields = [
            'title',
            'amount',
            'source',
            'date',
            'description',
        ]

        widgets = {

            'title': forms.TextInput(attrs={
                'placeholder': 'e.g. Pocket Money',
                'class': 'form-input',
            }),

            'amount': forms.NumberInput(attrs={
                'placeholder': 'e.g. 5000',
                'step': '0.01',
                'min': '0.01',
                'class': 'form-input',
            }),

            'source': forms.Select(attrs={
                'class': 'form-input',
            }),

            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-input',
                }
            ),

            'description': forms.Textarea(attrs={
                'placeholder': 'Optional description',
                'rows': 4,
                'class': 'form-input',
            }),
        }


class BudgetForm(forms.ModelForm):

    class Meta:
        model = Budget

        fields = [
            'category',
            'amount',
            'month',
        ]

        widgets = {

            'category': forms.Select(attrs={
                'class': 'form-input',
            }),

            'amount': forms.NumberInput(attrs={
                'placeholder': 'e.g. 5000',
                'step': '0.01',
                'min': '0.01',
                'class': 'form-input',
            }),

            'month': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-input',
                }
            ),
        }