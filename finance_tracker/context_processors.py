from .models import Wallet


def total_balance(request):

    if request.user.is_authenticated:

        wallets = Wallet.objects.filter(owner=request.user)

        total = 0

        for wallet in wallets:
            total += wallet.balance

    else:
        total = 0

    return {
        "total_balance": total
    }