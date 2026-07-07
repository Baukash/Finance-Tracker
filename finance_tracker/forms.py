from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Wallet, Expense, Budget, Category


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class WalletForm(forms.ModelForm):

    class Meta:
        model = Wallet
        fields = ["name", "balance"]
        
class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ["date", "category", "wallet", "amount", "description"]
    
    def __init__(self, *args, **kwargs):

        user = kwargs.pop("user", None)

        super().__init__(*args, **kwargs)

        if user:
            self.fields["wallet"].queryset = Wallet.objects.filter(owner=user)
            self.fields["category"].queryset = Category.objects.filter(owner=user)



class BudgetForm(forms.ModelForm):

    class Meta:
        model = Budget
        fields = ["limit"]

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ["name"]