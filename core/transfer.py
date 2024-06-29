from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from decimal import Decimal

from account.models import Account
from .models import Transaction


@login_required
def search_users_account_number(request):

    accounts = Account.objects.all()
    query = request.POST.get("account_number")

    if query :
        accounts = Account.objects.filter(
            Q(account_number=query)|
            Q(account_id=query)
        )

    context = {
        'accounts' : accounts,
        'query' : query,
    }

    return render (request, 'transfer/search-user-by-account-number.html', context)


@login_required
def AmountTransfer(request, account_number):
    try:
        account = Account.objects.get(account_number=account_number)
    except:
        account= None
        messages.warning(request, 'Account does not exist.')
        return redirect('core:search-account')

    context = {
        'account': account
    }
    return render(request, "transfer/amount-transfer.html", context)


@login_required
def AmountTransferProcess(request, account_number):
    account = Account.objects.get(account_number=account_number)
    sender = request.user
    reciever = account.user

    sender_account = request.user.account
    # reciever_account = account

    if request.method == "POST":
        amount = request.POST.get("amound-send")
        description = request.POST.get("description")

        if Decimal(amount) > 0 and sender_account.account_balance > Decimal(amount)  :
            new_transaction = Transaction.objects.create(
                user = request.user,
                amount = amount,
                description = description,
                reciever = reciever,
                sender = sender,
                sender_account = sender_account,
                reciever_account = account,
                status = "processing",
                transaction_type = "transfer",
              
            )
            new_transaction.save()

            transaction_id = new_transaction.transaction_id
            return redirect("core:transfer-confirmation", account.account_number, transaction_id)
        
        else :
            messages.warning(request, "Insufficient Fund.")
            return redirect('core:amount-transfer', account.account_number)
        
    else :
        messages.warning(request, "Error Occured, Try again later.")
        return redirect('account:account')
        
@login_required
def TransferConfirmation(request, account_number, transaction_id):
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transaction.objects.get(transaction_id=transaction_id)
    except:
        messages.warning(request, "Transaction does not exist.")
        return redirect('account:account')
    
    context = {
        'account':account,
        'transaction':transaction,
    }
    
    return render (request, 'transfer/transfer-confirmation.html', context)


@login_required
def TransferProcess(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    sender = request.user
    reciever = account.user

    sender_account = request.user.account
    reciever_account = account

    complated = False

    if request.method == "POST" :
        pin_number = request.POST.get('pin-number')

        if pin_number == sender_account.pin_number :
            transaction.status = "completed"
            transaction.save()

            # Remove the amount that i am sending from my account balance and update my account
            sender_account.account_balance -= transaction.amount
            sender_account.save()

            # Add the amount that was removed from my account to the person that i am sending the money
            account.account_balance += transaction.amount
            account.save()

            messages.success(request, "Transfer Successful.")
            return redirect("core:transfer-complated", account.account_number, transaction.transaction_id )
        
        else :
            messages.warning(request, "Incorrect Pin")
            return redirect("core:transfer-confirmation", account.account_number, transaction.transaction_id )
        
    else :
        messages.warning(request, "An error occured, Try again later.")
        return redirect("account:account")





@login_required
def TransferComplated(request, account_number, transaction_id):
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transaction.objects.get(transaction_id=transaction_id)
    except:
        messages.warning(request, "Transfer does not exist.")
        return redirect('account:account')
    
    context = {
        'account':account,
        'transaction':transaction,
    }
    
    return render (request, 'transfer/transfer-complated.html', context)

