from django.urls import path

from .views import login_user, register, log_out, user_account_main_page, edit_user_profile, add_product

urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register),
    path('log-out', log_out),
    path('user', user_account_main_page),
    path('user/edit', edit_user_profile),
    path('user/add_product', add_product)
]
