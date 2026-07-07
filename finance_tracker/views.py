from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from .forms import RegisterForm, WalletForm, ExpenseForm
from .models import Wallet, Expense
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

@login_required
def wallets(request):
    wallets = Wallet.objects.filter(owner=request.user)

    return render(request, "wallets.html", {
        "wallets": wallets
    })


@login_required
def add_wallet(request):

    if request.method == "POST":

        form = WalletForm(request.POST)

        if form.is_valid():

            wallet = form.save(commit=False)
            wallet.owner = request.user
            wallet.save()

            return redirect("wallets")

    else:
        form = WalletForm()

    return render(request, "wallet_form.html", {
        "form": form
    })

@login_required
def edit_wallet(request, id):

    wallet = get_object_or_404(
        Wallet,
        id=id,
        owner=request.user
    )

    if request.method == "POST":

        form = WalletForm(request.POST, instance=wallet)

        if form.is_valid():

            form.save()
            return redirect("wallets")

    else:

        form = WalletForm(instance=wallet)

    return render(request, "wallet_form.html", {
        "form": form
    })

@login_required
def delete_wallet(request, id):

    wallet = get_object_or_404(
        Wallet,
        id=id,
        owner=request.user
    )

    if request.method == "POST":

        wallet.delete()
        return redirect("wallets")

    return render(request, "delete_wallet.html", {
        "wallet": wallet
    })

@login_required
def expenses(request):
    expenses = Expense.objects.filter(owner=request.user)

    return render(request, "expenses.html", {
        "expenses": expenses
    })

@login_required
def add_expense(request):

    if request.method == "POST":

        form = ExpenseForm(request.POST, user=request.user)

        if form.is_valid():

            expense = form.save(commit=False)
            expense.owner = request.user

            wallet = expense.wallet
            wallet.balance -= expense.amount
            wallet.save()

            expense.save()

            return redirect("expenses")

    else:
        form = ExpenseForm(user=request.user)

    return render(request, "expense_form.html", {
        "form": form
    })

@login_required
def edit_expense(request, id):

    expense = get_object_or_404(
        Expense,
        id=id,
        owner=request.user
    )

    if request.method == "POST":

        original_wallet = expense.wallet
        original_amount = expense.amount

        form = ExpenseForm(
            request.POST,
            instance=expense,
            user=request.user
        )

        if form.is_valid():

            expense = form.save(commit=False)

            if original_wallet.pk != expense.wallet.pk:
                original_wallet.balance += original_amount
                original_wallet.save()

                # Subtract from the selected wallet
                expense.wallet.balance -= expense.amount
                expense.wallet.save()
            else:
                difference = expense.amount - original_amount
                expense.wallet.balance -= difference
                expense.wallet.save()

            

            expense.save()

            return redirect("expenses")

    else:

        form = ExpenseForm(
            instance=expense,
            user=request.user
        )

    return render(request, "expense_form.html", {
        "form": form
    })

@login_required
def delete_expense(request, id):

    expense = get_object_or_404(Expense, id=id, owner=request.user)

    if request.method == "POST":

        wallet = expense.wallet

        wallet.balance += expense.amount
        wallet.save()

        expense.delete()
        return redirect("expenses")

    return render(request, "delete.html", {
        "expense": expense
    })

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home")