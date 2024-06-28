from django.urls import path

from . import views, transfer

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),


    # Transfer :
    path('search-account/', transfer.search_users_account_number, name='search-account'),
    path('amount-transfer/<account_number>/', transfer.AmountTransfer, name='amount-transfer'),
    path('amount-transfer-process/<account_number>/', transfer.AmountTransferProcess, name='amount-transfer-process'),


    # Request Money :


    # Add debit Card :
]
