from django.urls import path
from . import api_views

urlpatterns = [
    path("expenses/", api_views.expense_api),
    path("wallets/", api_views.WalletAPIView.as_view()),
]