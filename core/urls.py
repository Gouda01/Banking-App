from django.urls import path

from . import views, transfer, transaction, payment_request

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),


    # Transfer :
    path('search-account/', transfer.search_users_account_number, name='search-account'),
    path('amount-transfer/<account_number>/', transfer.AmountTransfer, name='amount-transfer'),
    path('amount-transfer-process/<account_number>/', transfer.AmountTransferProcess, name='amount-transfer-process'),
    path('transfer-confirmation/<account_number>/<transaction_id>/', transfer.TransferConfirmation, name='transfer-confirmation'),
    path('transfer-process/<account_number>/<transaction_id>/', transfer.TransferProcess, name='transfer-process'),
    path('transfer-complated/<account_number>/<transaction_id>/', transfer.TransferComplated, name='transfer-complated'),



    # Transactions:
    path('transactions/', transaction.transaction_lists, name='transactions'),
    path('transaction-detail/<transaction_id>', transaction.transaction_detail, name='transaction-detail'),


    # Payment Request :
    path('request-search-account/', payment_request.SearchUsersRequest, name='request-search-account'),
    path('amount-request/<account_number>/', payment_request.AmoundRequest, name='amount-request'),
    path('amount-request-process/<account_number>/', payment_request.AmountRequestProcess, name='amount-request-process'),
    path('amount-request-confirmation/<account_number>/<transaction_id>/', payment_request.AmountRequestConfirmation, name='amount-request-confirmation'),
    path('amount-request-final-process/<account_number>/<transaction_id>/', payment_request.AmountRequestFinalProcess, name='amount-request-final-process'),
    path('amount-request-completed/<account_number>/<transaction_id>/', payment_request.RequestCompleted, name='amount-request-completed'),


    # Add debit Card :
]
