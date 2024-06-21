from django.urls import path

from . import views, transfer

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),


    # Transfer :
    path('search-account', transfer.search_users_account_number, name='search-account'),


    # Request Money :


    # Add debit Card :
]
