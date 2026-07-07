from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("wallets/", views.wallets, name="wallets"),
    path("wallets/add/", views.add_wallet, name="add_wallet"),
    path("wallets/edit/<int:id>/", views.edit_wallet, name="edit_wallet"),
    path("wallets/delete/<int:id>/", views.delete_wallet, name="delete_wallet"),
]